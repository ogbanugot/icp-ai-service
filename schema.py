from typing import List

from pydantic import BaseModel, Field

class CVAnalysisRequest(BaseModel):
    job_title: str = ""
    experience_years: str = ""
    skills: str = ""
    current_role: str = ""
    job_description: str
    cv_text: str
    cv_template: str


class GrammarAnalysisRequest(BaseModel):
    text: str


class MacronutrientRatios(BaseModel):
    protein: str = "30%"
    carbs: str = "50%"
    fats: str = "20%"


class CookingAndPreparation(BaseModel):
    # "grilling", "steaming", "baking"
    cooking_methods: List[str]
    # 30 minutes
    prep_time: str


class MealPreferences(BaseModel):
    # "breakfast", "lunch", "dinner", "snacks"
    meal_types: List[str]
    # "8:00 AM", "12:00 PM", "6:00 PM"
    meal_times: List[str]


class FoodAvailability(BaseModel):
    seasonal_ingredients: List[str]
    local_produce: List[str]


class PortionSizes(BaseModel):
    serving_sizes: List[str]


class UserPreferences(BaseModel):
    dietary_restrictions: str
    allergies: str
    favorite_foods: str
    disliked_foods: str
    mealPlan_purpose: str
    country: str


class NutritionalGoals(BaseModel):
    caloric_intake: int


class MealPlanRequest(BaseModel):
    meal_title: str
    user_preferences: UserPreferences
    nutritional_goals: NutritionalGoals

class JobReadiness(BaseModel):
	"""Job readiness model"""
	enhanced_cv: str = Field(..., description="Created enhanced cv by strategist agent")
	#original_ats_score: str = Field(..., description="Original cv ats score")
	enhanced_ats_score: str = Field(..., description="Enhanced cv ats score by ats evaluator agent")
	interview_prep: str = Field(..., description="Interview preparation questions by interview preparer agent")

