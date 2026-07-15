# ==========================================
# CareerPilot AI - Project Recommendation
# ==========================================

project_database = {

    "Data Scientist": [

        {
            "title": "Student Performance Prediction",
            "description": "Predict student marks using Machine Learning.",
            "difficulty": "Intermediate",
            "duration": "5-7 Days",
            "skills": ["Python", "Pandas", "Scikit Learn"],
            "learning": [
                "Data Cleaning",
                "Regression",
                "Model Evaluation"
            ]
        },

        {
            "title": "Customer Churn Prediction",
            "description": "Predict whether a customer will leave a company.",
            "difficulty": "Intermediate",
            "duration": "1 Week",
            "skills": ["Python", "SQL", "Machine Learning"],
            "learning": [
                "Classification",
                "Feature Engineering",
                "Data Visualization"
            ]
        },

        {
            "title": "House Price Prediction",
            "description": "Predict house prices using regression algorithms.",
            "difficulty": "Beginner",
            "duration": "4 Days",
            "skills": ["Python", "Pandas", "Regression"],
            "learning": [
                "Regression",
                "Data Analysis"
            ]
        }

    ],

    "Machine Learning Engineer": [

        {
            "title": "Fake News Detection",
            "description": "Detect fake news using NLP.",
            "difficulty": "Advanced",
            "duration": "10 Days",
            "skills": ["Python", "NLP", "Scikit Learn"],
            "learning": [
                "Natural Language Processing",
                "Text Classification"
            ]
        },

        {
            "title": "Image Classification",
            "description": "Classify images using Deep Learning.",
            "difficulty": "Advanced",
            "duration": "2 Weeks",
            "skills": ["TensorFlow", "CNN", "Python"],
            "learning": [
                "CNN",
                "Image Processing",
                "Deep Learning"
            ]
        },

        {
            "title": "Spam Email Detection",
            "description": "Detect spam emails using Machine Learning.",
            "difficulty": "Intermediate",
            "duration": "1 Week",
            "skills": ["Python", "Scikit Learn"],
            "learning": [
                "Classification",
                "Text Processing"
            ]
        }

    ],

    "Web Developer": [

        {
            "title": "Personal Portfolio Website",
            "description": "Create your own responsive portfolio.",
            "difficulty": "Beginner",
            "duration": "3 Days",
            "skills": ["HTML", "CSS", "JavaScript"],
            "learning": [
                "Responsive Design",
                "Frontend Development"
            ]
        },

        {
            "title": "E-Commerce Website",
            "description": "Develop a complete online shopping website.",
            "difficulty": "Intermediate",
            "duration": "2 Weeks",
            "skills": ["React", "Node.js", "MongoDB"],
            "learning": [
                "Full Stack Development",
                "Database Design"
            ]
        },

        {
            "title": "Hospital Management System",
            "description": "Manage patients, doctors and appointments.",
            "difficulty": "Advanced",
            "duration": "3 Weeks",
            "skills": ["React", "Node.js", "MongoDB"],
            "learning": [
                "Authentication",
                "CRUD Operations",
                "REST APIs"
            ]
        }

    ],

    "Cyber Security Analyst": [

        {
            "title": "Password Strength Checker",
            "description": "Analyze password security.",
            "difficulty": "Beginner",
            "duration": "2 Days",
            "skills": ["Python"],
            "learning": [
                "Regex",
                "Security Rules"
            ]
        },

        {
            "title": "Network Port Scanner",
            "description": "Scan open ports on a network.",
            "difficulty": "Intermediate",
            "duration": "1 Week",
            "skills": ["Python", "Networking"],
            "learning": [
                "Sockets",
                "Networking"
            ]
        }

    ],

    "Cloud Engineer": [

        {
            "title": "AWS EC2 Deployment",
            "description": "Deploy applications on AWS EC2.",
            "difficulty": "Intermediate",
            "duration": "1 Week",
            "skills": ["AWS", "Linux"],
            "learning": [
                "Cloud Deployment",
                "Virtual Machines"
            ]
        },

        {
            "title": "Docker Container Deployment",
            "description": "Containerize applications using Docker.",
            "difficulty": "Intermediate",
            "duration": "5 Days",
            "skills": ["Docker", "Linux"],
            "learning": [
                "Containers",
                "Docker Images"
            ]
        }

    ]

}


def recommend_projects(career):

    return project_database.get(career, [])