from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from fastapi import Request
from slowapi import Limiter
from slowapi.util import get_remote_address

from schema import CVAnalysisRequest, GrammarAnalysisRequest, MealPlanRequest, JobReadiness
from services.cv import cv_cmd, CVAnalysis
from services.grammar import grammar_cmd, GrammarAnalysis
from services.diet import meal_plan_cmd, MealPlan
from services.ml import main
from dotenv import load_dotenv
from services.cv_enhancer import enhancer_agent

load_dotenv()

app = FastAPI()

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/cv-analysis")
@limiter.limit("10/minute")
def cv_analysis(
        request: Request,
        data: CVAnalysisRequest
) -> CVAnalysis:
    try:
        cmd = cv_cmd(data)
        data = main(cmd)
        if len(data) >= 1:
            return data[0]
        else:
            raise HTTPException(status_code=500, detail="error during function call")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/grammar-analysis")
@limiter.limit("10/minute")
def grammar_analysis(
        request: Request,
        data: GrammarAnalysisRequest
) -> GrammarAnalysis:
    try:
        cmd = grammar_cmd(data)
        data = main(cmd)
        if len(data) >= 1:
            return data[0]
        else:
            raise HTTPException(status_code=500, detail="error during function call")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/meal-plan")
@limiter.limit("10/minute")
def meal_plan(
        request: Request,
        data: MealPlanRequest
) -> MealPlan:
    try:
        cmd = meal_plan_cmd(data)
        data = main(cmd)
        if len(data) >= 1:
            return data[0]
        else:
            raise HTTPException(status_code=500, detail="error during function call")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("/cv-enhancer")
@limiter.limit("10/minute")
def cv_analysis(
        request: Request,
        data: CVAnalysisRequest
) -> JobReadiness:
    try:
        result = enhancer_agent(data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))