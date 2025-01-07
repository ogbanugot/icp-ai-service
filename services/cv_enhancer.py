from schema import CVAnalysisRequest
from services.cv_crew import ResumeCrew

def enhancer_agent(req: CVAnalysisRequest):
    resume_crew = ResumeCrew()

    if req.cv_template not in resume_crew.cv_templates:
        req.cv_template = "DEFAULT"

        
    template_file = f"services/templates/{req.cv_template.lower()}.md"

    with open(template_file, 'r') as f:
        cv_template = f.read()

    inputs = {
        'job_description': req.job_description,
        'applicant_cv': req.cv_text,
        'cv_template': cv_template,
        }

    ### this execution will take a few minutes to run
    resume_crew.crew().kickoff(inputs=inputs)

    return resume_crew.tasks_output()
