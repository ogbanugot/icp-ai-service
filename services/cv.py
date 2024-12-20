from pydantic import BaseModel

from schema import CVAnalysisRequest


class CVAnalysis(BaseModel):
    work_experience: str
    skills: str
    suggestions: str


def edit_cv():
    return {
        "type": "function",
        "function": {
            "name": "provide_edited_cv",
            "description": "Edit the CV to better match the job description",
            "parameters": {
                "type": "object",
                "properties": {
                    "work_experience": {
                        "type": "string",
                        "description": "the edited work experience matching the job description",
                    },
                    "skills": {
                        "type": "string",
                        "description": "the edited skills to better match the job description",
                    },
                    "suggestions": {
                        "type": "string",
                        "description": "general suggestions to improve the CV",
                    },
                },
                "required": ["work_experience, skills", "suggestions"],
            },
        },
    }


def provide_edited_cv(data: CVAnalysis):
    return data


def cv_cmd(req: CVAnalysisRequest):
    prompt = f"You are a Certified Professional Resume Writer, with over 20 years experience in writing resume for job seeker in different industries for diverse job roles. Given this job description: {req.job_description} and job title {req.job_title}. " \
            f"In not more than 500 words, by utilising your creative and years of experience, rewrite this CV: {req.cv_text}, to better match the job description. I have {req.experience_years} combined years of experience in these skillset: {req.skills}. My current job role is {req.current_role} Use function calling to output your response in desired format."
    
    #prompt = f"Given this job description: {req.job_description} and job title {req.job_title}. " \
    #         f"Edit this CV: {req.cv_text}, to better match the job description."
    return prompt
