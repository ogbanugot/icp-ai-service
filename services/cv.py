from pydantic import BaseModel

from schema import CVAnalysisRequest


class CVAnalysis(BaseModel):
    work_experience: str
    skills: str
    professional_summary: str


def edit_cv():
    return {
        "type": "function",
        "function": {
            "name": "provide_edited_cv",
            "description": "Revamp the CV to better match the job description",
            "parameters": {
                "type": "object",
                "properties": {
                    "work_experience": {
                        "type": "string",
                        "description": "A list of various work experience from the CV, revamped to better match the "
                                       "job description. "
                                       "Make sure the list is formatted properly to include relevant information like "
                                       "the job title, duration and duties performed.",
                    },
                    "skills": {
                        "type": "string",
                        "description": "the edited skills to better match the job description",
                    },
                    "professional_summary": {
                        "type": "string",
                        "description": "A well written professional summary that aligns the CV with the job "
                                       "description.",
                    },
                },
                "required": ["work_experience", "skills", "professional_summary"],
            },
        },
    }


def provide_edited_cv(data: CVAnalysis):
    return data


def cv_cmd(req: CVAnalysisRequest):
    prompt = f"Given this job description: {req.job_description} and job title {req.job_title}. " \
             f"Revamp this CV: {req.cv_text}, to better match the job description."
    return prompt
