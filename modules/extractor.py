import re

# ==========================================
# Email
# ==========================================

def extract_email(text):

    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


# ==========================================
# Phone Number
# ==========================================

def extract_phone(text):

    pattern = r"(\+91[- ]?)?[6-9]\d{9}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


# ==========================================
# LinkedIn
# ==========================================

def extract_linkedin(text):

    pattern = r"(https?://)?(www\.)?linkedin\.com/in/[A-Za-z0-9_-]+"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


# ==========================================
# GitHub
# ==========================================

def extract_github(text):

    pattern = r"(https?://)?(www\.)?github\.com/[A-Za-z0-9_-]+"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


# ==========================================
# Name
# ==========================================

def extract_name(text):

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if len(line.split()) >= 2 and len(line) <= 40:

            if (
                "@" not in line
                and not any(char.isdigit() for char in line)
                and "linkedin" not in line.lower()
                and "github" not in line.lower()
            ):

                return line

    return "Not Found"


# ==========================================
# Skills
# ==========================================

def extract_skills(text):

    skills_database = [

        "Python",
        "Java",
        "C",
        "C++",
        "SQL",
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Node.js",
        "Flask",
        "Django",
        "Machine Learning",
        "Deep Learning",
        "Artificial Intelligence",
        "Data Science",
        "Power BI",
        "Tableau",
        "Excel",
        "Pandas",
        "NumPy",
        "Scikit Learn",
        "TensorFlow",
        "PyTorch",
        "Git",
        "GitHub",
        "MongoDB",
        "MySQL",
        "AWS",
        "Azure",
        "Docker",
        "Kubernetes",
        "Linux",
        "Networking",
        "Cyber Security"
    ]

    found_skills = []

    lower_text = text.lower()

    for skill in skills_database:

        if skill.lower() in lower_text:

            found_skills.append(skill)

    return found_skills


# ==========================================
# Education
# ==========================================

def extract_education(text):

    education_keywords = [

        "Bachelor",
        "Master",
        "B.Tech",
        "M.Tech",
        "B.Sc",
        "M.Sc",
        "BCA",
        "MCA",
        "Computer Science",
        "Engineering",
        "Higher Secondary",
        "HSC",
        "SSLC",
        "CBSE"
    ]

    education = []

    lower_text = text.lower()

    for item in education_keywords:

        if item.lower() in lower_text:

            education.append(item)

    return education


# ==========================================
# Projects
# ==========================================

def extract_projects(text):

    lines = text.split("\n")

    projects = []

    collect = False

    for line in lines:

        line = line.strip()

        if line.lower() in ["project", "projects"]:

            collect = True
            continue

        if collect:

            if line == "":
                break

            projects.append(line)

    return projects


# ==========================================
# Master Function
# ==========================================

def extract_resume_details(text):

    details = {

        "Name": extract_name(text),
        "Email": extract_email(text),
        "Phone": extract_phone(text),
        "LinkedIn": extract_linkedin(text),
        "GitHub": extract_github(text),
        "Skills": extract_skills(text),
        "Education": extract_education(text),
        "Projects": extract_projects(text)

    }

    return details