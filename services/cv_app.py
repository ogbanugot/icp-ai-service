from cv_crew import ResumeCrew

resume_crew = ResumeCrew()

inputs = {
    'job_description': """
        Job Description:

        Job Title: Software Engineer (Backend)

        Company: Innovatech Solutions

        Location: Lagos, Nigeria

        Job Type: Full-time

        About the Company: Innovatech Solutions is a leading technology company that provides innovative solutions for businesses. We're looking for a skilled Software Engineer (Backend) to join our team.

        Job Summary:

        We're seeking a highly motivated and experienced Software Engineer (Backend) to design, develop, and deploy scalable and efficient backend systems. The ideal candidate should have a strong background in software development, programming languages, and database management.

        Responsibilities:

            Design, develop, and deploy backend systems using Java, Python, or NodeJS
            Collaborate with cross-functional teams to design and implement software features
            Develop and maintain high-quality, scalable, and efficient software systems
            Troubleshoot and debug issues in the backend systems
            Develop and enforce design patterns and coding standards
            Work with the security team to ensure the security and integrity of our systems
            Stay up-to-date with the latest technologies and trends in software development

        Requirements:

            Bachelor's degree in Computer Science, Software Engineering, or related field
            3+ years of experience in software development
            Strong background in programming languages, data structures, and algorithms
            Experience with databases, including SQL and NoSQL
            Strong understanding of cloud computing platforms (AWS, Azure, or Google Cloud)
            Knowledge of Agile development methodologies
            Excellent problem-solving skills and attention to detail

        Nice to Have:

            Experience with DevOps tools and automation scripts
            Knowledge of containerization using Docker
            Familiarity with machine learning and artificial intelligence concepts

        Benefits:

            Competitive salary and benefits package
            Opportunity to work on exciting projects and contribute to the growth of a leading technology company
            Collaborative and dynamic team environment
            Professional development and training opportunities
            Flexible working hours and remote work options

        How to Apply:

        Send your resume and a cover letter to careers@innovatech.com. We can't wait to hear from you!
    """,
    'applicant_cv': """
        Resume:

        John Doe

        Address: 12, Funmi Abisogulu Street, Ojodu, Lagos

        Phone: +234 816 654 321

        Email: john.doe@gmail.com

        Summary:

        Highly motivated and experienced software engineer with 5+ years of experience in designing, developing, and deploying scalable and efficient backend systems. Skilled in programming languages, data structures, and algorithms. Strong understanding of cloud computing platforms and Agile development methodologies.

        Education:

            Bachelor of Science in Computer Science, University of Lagos (2015-2019)

        Experience:

            Software Engineer (Backend), Tech Solutions Limited (2020-Present)
                Designed, developed, and deployed high-quality, scalable, and efficient backend systems using Java, Python, and NodeJS
                Collaborated with cross-functional teams to design and implement software features
                Troubleshoot and debug issues in the backend systems
                Developed and enforced design patterns and coding standards
            Junior Software Engineer (Backend), XYZ Corporation (2019-2020)
                Developed and deployed backend systems using Java and Python
                Worked on integration projects with other teams
                Participated in code reviews and ensured adherence to coding standards

        Skills:

            Programming languages: Java, Python, NodeJS
            Data structures and algorithms: Arrays, Linked Lists, Trees, and Graphs
            Database management: SQL and NoSQL
            Cloud computing platforms: AWS, Azure
            Agile development methodologies: Scrum, Kanban
            DevOps tools: Docker, Jenkins
            Strong understanding of security and cryptography concepts

        Certifications:

            Certified Java Developer, Oracle University (2020)
            Certified Python Developer, Python Institute (2021)

        References:

        Available upon request.
        """
    }

def kickoff():
    ### this execution will take a few minutes to run
    output = resume_crew.crew().kickoff(inputs=inputs)

    #job_readiness = resume_crew.tasks_output()
    #print(job_readiness.json())
    print("before the output")
    print(output)

if __name__ == "__main__":
    kickoff()