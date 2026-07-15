# ==========================================
# CareerPilot AI - Career Recommendation
# ==========================================

career_database = {

    "Data Scientist": {

        "skills": [
            "Python",
            "SQL",
            "Pandas",
            "NumPy",
            "Machine Learning",
            "Power BI",
            "Tableau"
        ],

        "roadmap": [
            "Master Python",
            "Learn NumPy & Pandas",
            "Master SQL",
            "Learn Data Visualization",
            "Learn Machine Learning",
            "Build 5 Data Science Projects",
            "Participate in Kaggle",
            "Create Portfolio",
            "Apply for Data Scientist Roles"
        ],

        "certifications": [
            "Google Data Analytics",
            "IBM Data Science",
            "Microsoft Power BI"
        ]

    },

    "Machine Learning Engineer": {

        "skills": [
            "Python",
            "Machine Learning",
            "TensorFlow",
            "PyTorch",
            "Scikit Learn",
            "Deep Learning"
        ],

        "roadmap": [
            "Master Python",
            "Study Statistics",
            "Learn Machine Learning",
            "Master TensorFlow",
            "Learn PyTorch",
            "Deploy ML Models",
            "Build Portfolio"
        ],

        "certifications": [
            "Google ML",
            "AWS ML Specialty"
        ]

    },

    "Web Developer": {

        "skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Node.js",
            "MongoDB"
        ],

        "roadmap": [
            "Master HTML",
            "Master CSS",
            "Learn JavaScript",
            "Learn React",
            "Learn Node.js",
            "Learn MongoDB",
            "Deploy Full Stack Projects"
        ],

        "certifications": [
            "Meta Frontend",
            "Meta Backend"
        ]

    },

    "Cyber Security Analyst": {

        "skills": [
            "Python",
            "Linux",
            "Networking",
            "Cyber Security"
        ],

        "roadmap": [
            "Learn Networking",
            "Master Linux",
            "Study Ethical Hacking",
            "Practice CTF Challenges",
            "Earn Security Certifications"
        ],

        "certifications": [
            "CompTIA Security+",
            "CEH"
        ]

    },

    "Cloud Engineer": {

        "skills": [
            "AWS",
            "Azure",
            "Docker",
            "Kubernetes",
            "Linux"
        ],

        "roadmap": [
            "Master Linux",
            "Learn AWS",
            "Learn Azure",
            "Learn Docker",
            "Learn Kubernetes",
            "Learn CI/CD",
            "Deploy Cloud Applications"
        ],

        "certifications": [
            "AWS Cloud Practitioner",
            "AWS Solutions Architect",
            "Azure AZ-900"
        ]

    }

}


def recommend_career(user_skills):

    best_career = None
    best_score = 0
    missing_skills = []

    user_skills = [skill.lower() for skill in user_skills]

    for career, details in career_database.items():

        required = [skill.lower() for skill in details["skills"]]

        matched = len(set(user_skills).intersection(required))

        percentage = (matched / len(required)) * 100

        if percentage > best_score:

            best_score = percentage
            best_career = career

            missing_skills = [
                skill for skill in details["skills"]
                if skill.lower() not in user_skills
            ]

    if best_career is None:

        return {

            "career": "No Recommendation",
            "percentage": 0,
            "missing": [],
            "roadmap": [],
            "certifications": []

        }

    return {

        "career": best_career,
        "percentage": round(best_score),
        "missing": missing_skills,
        "roadmap": career_database[best_career]["roadmap"],
        "certifications": career_database[best_career]["certifications"]

    }