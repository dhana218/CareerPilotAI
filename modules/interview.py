# ==========================================
# CareerPilot AI - Interview Questions
# ==========================================

interview_database = {

    "Data Scientist": [

        {
            "question": "What is Data Science?",
            "answer": "Data Science is the process of extracting useful insights from data using statistics, programming and machine learning."
        },

        {
            "question": "Difference between Supervised and Unsupervised Learning?",
            "answer": "Supervised learning uses labeled data while unsupervised learning uses unlabeled data."
        },

        {
            "question": "What is Pandas?",
            "answer": "Pandas is a Python library used for data manipulation and analysis."
        },

        {
            "question": "What is NumPy?",
            "answer": "NumPy is a Python library used for numerical computations and array operations."
        },

        {
            "question": "What is Overfitting?",
            "answer": "Overfitting occurs when a model learns the training data too well and performs poorly on new data."
        },

        {
            "question": "Explain Regression.",
            "answer": "Regression predicts continuous numerical values."
        },

        {
            "question": "What is Classification?",
            "answer": "Classification predicts categorical outputs such as Yes/No."
        },

        {
            "question": "What is SQL used for?",
            "answer": "SQL is used to store, retrieve and manipulate data in databases."
        },

        {
            "question": "What is Feature Engineering?",
            "answer": "Feature engineering is creating useful input variables that improve model performance."
        },

        {
            "question": "Tell me about one of your Data Science projects.",
            "answer": "Explain your project, dataset, preprocessing, model, evaluation and results."
        }

    ],

    "Machine Learning Engineer": [

        {
            "question":"What is Machine Learning?",
            "answer":"Machine Learning enables computers to learn from data without explicit programming."
        },

        {
            "question":"Explain Bias and Variance.",
            "answer":"Bias is error due to overly simple assumptions, variance is error due to sensitivity to training data."
        },

        {
            "question":"What is TensorFlow?",
            "answer":"TensorFlow is Google's deep learning framework."
        },

        {
            "question":"What is PyTorch?",
            "answer":"PyTorch is Meta's deep learning library widely used for research."
        },

        {
            "question":"Explain Gradient Descent.",
            "answer":"Gradient Descent minimizes loss by updating model parameters."
        },

        {
            "question":"What is CNN?",
            "answer":"CNN is a deep learning architecture mainly used for image processing."
        },

        {
            "question":"Difference between AI, ML and DL?",
            "answer":"AI is the broader field, ML is a subset of AI, DL is a subset of ML."
        },

        {
            "question":"What is Cross Validation?",
            "answer":"It evaluates model performance using multiple train-test splits."
        },

        {
            "question":"What is Model Deployment?",
            "answer":"Making a trained model available for real-world use."
        },

        {
            "question":"Explain one ML project you built.",
            "answer":"Describe the problem, dataset, algorithm and evaluation."
        }

    ],

    "Web Developer":[
        {"question":"What is HTML?","answer":"HTML structures web pages."},
        {"question":"Difference between HTML and CSS?","answer":"HTML creates structure, CSS styles it."},
        {"question":"What is JavaScript?","answer":"JavaScript adds interactivity."},
        {"question":"What is React?","answer":"React is a JavaScript library for building user interfaces."},
        {"question":"What is Node.js?","answer":"Node.js runs JavaScript on the server."},
        {"question":"What is REST API?","answer":"REST is an architecture for web services."},
        {"question":"What is MongoDB?","answer":"MongoDB is a NoSQL database."},
        {"question":"Explain responsive design.","answer":"Responsive design adapts websites to different screen sizes."},
        {"question":"Difference between GET and POST?","answer":"GET retrieves data, POST sends data."},
        {"question":"Describe your web project.","answer":"Explain technologies, architecture and challenges."}
    ],

    "Cyber Security Analyst":[
        {"question":"What is Cyber Security?","answer":"Protecting systems and networks from attacks."},
        {"question":"What is Phishing?","answer":"A social engineering attack to steal information."},
        {"question":"What is Malware?","answer":"Malicious software that harms systems."},
        {"question":"What is Firewall?","answer":"A firewall monitors and filters network traffic."},
        {"question":"What is Encryption?","answer":"Converting data into unreadable form."},
        {"question":"Difference between Virus and Worm?","answer":"A virus needs a host; a worm spreads independently."},
        {"question":"What is VPN?","answer":"A Virtual Private Network secures internet communication."},
        {"question":"What is SQL Injection?","answer":"An attack that manipulates SQL queries."},
        {"question":"Explain OWASP.","answer":"OWASP publishes web security best practices."},
        {"question":"Describe a security project.","answer":"Explain the problem, tools and outcome."}
    ],

    "Cloud Engineer":[
        {"question":"What is Cloud Computing?","answer":"Delivering computing services over the internet."},
        {"question":"What is AWS?","answer":"Amazon Web Services is a cloud platform."},
        {"question":"What is Azure?","answer":"Microsoft Azure is a cloud platform."},
        {"question":"What is Docker?","answer":"Docker packages applications into containers."},
        {"question":"What is Kubernetes?","answer":"Kubernetes manages containerized applications."},
        {"question":"Difference between VM and Container?","answer":"VM virtualizes hardware; containers share the host OS."},
        {"question":"What is EC2?","answer":"Amazon EC2 provides virtual servers."},
        {"question":"What is S3?","answer":"Amazon S3 is object storage."},
        {"question":"What is CI/CD?","answer":"Continuous Integration and Continuous Deployment automate software delivery."},
        {"question":"Describe a cloud project.","answer":"Explain architecture, services used and deployment."}
    ]
}


def get_interview_questions(career):
    return interview_database.get(career, [])