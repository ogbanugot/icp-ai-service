from schema import CVAnalysisRequest
from services.cv_crew import ResumeCrew

def enhancer_agent(req: CVAnalysisRequest):
    resume_crew = ResumeCrew()

    inputs = {
        'job_description': req.job_description,
        'applicant_cv': req.cv_text
        }

    ### this execution will take a few minutes to run
    resume_crew.crew().kickoff(inputs=inputs)

    return resume_crew.tasks_output()
