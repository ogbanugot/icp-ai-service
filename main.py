from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi import Limiter
from slowapi.util import get_remote_address

from schema import CVAnalysisRequest, GrammarAnalysisRequest, MealPlanRequest
from services.cv import cv_cmd, CVAnalysis
from services.grammar import grammar_cmd, GrammarAnalysis
from services.diet import meal_plan_cmd, MealPlan
from services.ml import main
from dotenv import load_dotenv

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
@limiter.limit("300/minute")
def cv_analysis(
        request: Request,
        data: CVAnalysisRequest
) -> JSONResponse:
    try:
        cmd = cv_cmd(data)
        response_data = main(cmd)
        if len(response_data) >= 1:
            return JSONResponse(content=response_data[0].dict(), media_type="application/json")
        else:
            raise HTTPException(status_code=500, detail="Error during function call")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/grammar-analysis")
@limiter.limit("300/minute")
def grammar_analysis(
        request: Request,
        data: GrammarAnalysisRequest
) -> JSONResponse:
    try:
        cmd = grammar_cmd(data)
        response_data = main(cmd)
        if len(response_data) >= 1:
            return JSONResponse(content=response_data[0].dict(), media_type="application/json")
        else:
            raise HTTPException(status_code=500, detail="Error during function call")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/meal-plan")
@limiter.limit("300/minute")
def meal_plan(
        request: Request,
        data: MealPlanRequest
) -> JSONResponse:
    try:
        cmd = meal_plan_cmd(data)
        response_data = main(cmd)
        if len(response_data) >= 1:
            return JSONResponse(content=response_data[0].dict(), media_type="application/json")
        else:
            raise HTTPException(status_code=500, detail="Error during function call")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
