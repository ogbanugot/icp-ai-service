from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tasks.task_output import TaskOutput


import os
from services.utils import get_openai_api_key

from schema import JobReadiness

openai_api_key = get_openai_api_key()
model_name = os.getenv("MODEL_NAME")
os.environ["OPENAI_MODEL_NAME"] = f"openai/{model_name}"
os.environ["OPENAI_API_KEY"] = os.getenv("UNIFY_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("UNIFY_URL")

@CrewBase
class ResumeCrew:
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    job_analysis_task = Task
    profile_task = Task
    strategy_task = Task
    ats_evaluation_task = Task
    interview_preparation_task = Task

    cv_templates = ["NG","EU","CA","US","DEFAULT"]

    enhanced_cv = ""
	#original_ats_score: str = ""
    enhanced_ats_score = ""
    interview_prep = ""

    def strategy_callback(self, output: TaskOutput):
        self.enhanced_cv = output.raw

    def ats_callback(self, output: TaskOutput):
        self.enhanced_ats_score = output.raw

    def preparation_callback(self, output: TaskOutput):
        self.interview_prep = output.raw

    @agent
    def job_analyst(self) -> Agent:
        return Agent(
                config=self.agents_config['job_analyst'],
                tools=[],
                verbose=True,
                allow_delegation=False,
        )

    @agent
    def profiler(self) -> Agent:
        return Agent(
                config=self.agents_config['profiler'],
                tools=[],
                verbose=True,
                allow_delegation=False,
        )

    @agent
    def strategist(self) -> Agent:
        return Agent(
                config=self.agents_config['strategist'],
                tools=[],
                verbose=True,
                allow_delegation=False,
        )

    @agent
    def ats_evaluator(self) -> Agent:
        return Agent(
                config=self.agents_config['ats_evaluator'],
                tools=[],
                verbose=True,
                allow_delegation=False,
        )

    @agent
    def invterview_preparer(self) -> Agent:
        return Agent(
                config=self.agents_config['interview_preparer'],
                tools=[],
                verbose=True,
                allow_delegation=False,
        )
    
    @task
    def job_analysis(self) -> Task:
        self.job_analysis_task = Task(
                config=self.tasks_config['job_analysis'],
                agent=self.job_analyst()
        )

        return self.job_analysis_task

    @task
    def profile(self) -> Task:
        self.profile_task = Task(
                config=self.tasks_config['profile'],
                agent=self.profiler(),
                json_output=JobReadiness,
                #callback=self.profile_callback
        )

        return self.profile_task

    @task
    def strategy(self) -> Task:
        self.strategy_task = Task(
                config=self.tasks_config['strategy'],
                context=[self.job_analysis(), 
                         self.profile()],
                agent=self.strategist(),
                json_output=JobReadiness,
                callback=self.strategy_callback
        )

        return self.strategy_task

    @task
    def ats_evaluation(self) -> Task:
        self.ats_evaluation_task = Task(
                config=self.tasks_config['ats_evaluation'],
                context=[self.strategy()],
                agent=self.ats_evaluator(),
                json_output=JobReadiness,
                callback=self.ats_callback
        )

        return self.ats_evaluation_task

    @task
    def interview_preparation(self) -> Task:
        self.interview_preparation_task = Task(
                config=self.tasks_config['interview_preparation'],
                context=[
                        #self.job_analysis(), 
                        #self.profile(), 
                        self.strategy()
                         ],
                agent=self.invterview_preparer(),
                json_output=JobReadiness,
                callback=self.preparation_callback
        )

        return self.interview_preparation_task
    
    def tasks_output(self) -> JobReadiness:
        job_readiness = JobReadiness(
                enhanced_cv=self.strategy_task.output.raw,
                enhanced_ats_score=self.ats_evaluation_task.output.raw,
                interview_prep=self.interview_preparation_task.output.raw
            )

        return job_readiness

    
    @crew
    def crew(self) -> Crew:
        """Creates the ResumeCrew crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
            process=Process.sequential,
        )
