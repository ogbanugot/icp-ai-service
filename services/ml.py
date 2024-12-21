from typing import List, Optional

from dotenv import load_dotenv
from openai import OpenAI
import os
import json

from openai.types.chat import ChatCompletionMessageToolCall
from pydantic import ValidationError

from services.cv import edit_cv, CVAnalysis, provide_edited_cv
from services.grammar import grammar_check, GrammarAnalysis, provide_grammar_check
from services.diet import meal_plan, MealPlan, provide_meal_plan

load_dotenv()
model_name = os.getenv("MODEL_NAME")
unify_url = os.getenv("UNIFY_URL")
unify_api_key = os.getenv("UNIFY_API_KEY")

client = OpenAI(base_url=unify_url, api_key=unify_api_key)

tools_list = [edit_cv(), grammar_check(), meal_plan()]

fschemas = {
    "provide_edited_cv": CVAnalysis,
    "provide_grammar_check": GrammarAnalysis,
    "provide_meal_plan": MealPlan,
}

tools_schema = {
    "provide_edited_cv": provide_edited_cv,
    "provide_grammar_check": provide_grammar_check,
    "provide_meal_plan": provide_meal_plan,
}


def get_tool_call(command: str) -> Optional[List[ChatCompletionMessageToolCall]]:
    messages = [{"role": "user", "content": command}]
    tools = tools_list
    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        tools=tools,
        tool_choice="auto"
        #temperature=0.3,
        #max_tokens=500,
    )
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls
    return tool_calls


def call_tool(tool_calls: Optional[List[ChatCompletionMessageToolCall]]):
    if tool_calls:
        response = []
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = tools_schema[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_schema = fschemas[function_name]
            try:
                function_data_param = function_schema.parse_obj(function_args)
            except ValidationError as e:
                raise e
            function_response = function_to_call(
                function_data_param
            )
            response.append(function_response)
        return response
    else:
        raise "No tool_calls found"


def main(command: str):
    tools = get_tool_call(command)
    response = call_tool(tools)
    return response
