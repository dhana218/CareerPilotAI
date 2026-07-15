# ==========================================
# CareerPilot AI - ATS Score Module
# ==========================================

def calculate_ats_score(details, resume_text):
    score = 0
    comments = []

    text = resume_text.lower()

    # --------------------------------------
    # Contact Information
    # --------------------------------------

    if "@" in resume_text:
        score += 10
    else:
        comments.append("📧 Add a professional email address.")

    if "linkedin.com" in text:
        score += 10
    else:
        comments.append("🔗 Add your LinkedIn profile.")

    if "github.com" in text:
        score += 5
    else:
        comments.append("💻 Add your GitHub profile.")

    # --------------------------------------
    # Skills Section
    # --------------------------------------

    if "skills" in text or "skill" in text:
        score += 15
    else:
        comments.append("🛠 Add a Skills section.")

    # --------------------------------------
    # Education
    # --------------------------------------

    education_keywords = [
        "b.tech",
        "b.e",
        "b.sc",
        "bca",
        "mca",
        "m.tech",
        "master",
        "bachelor"
    ]

    if any(word in text for word in education_keywords):
        score += 15
    else:
        comments.append("🎓 Mention your educational qualification.")

    # --------------------------------------
    # Projects
    # --------------------------------------

    if "project" in text or "projects" in text:
        score += 20
    else:
        comments.append("📂 Add academic or personal projects.")

    # --------------------------------------
    # Experience
    # --------------------------------------

    if "experience" in text or "internship" in text:
        score += 10
    else:
        comments.append("💼 Add internships or work experience if available.")

    # --------------------------------------
    # Certifications
    # --------------------------------------

    if "certification" in text or "certificate" in text:
        score += 10
    else:
        comments.append("📜 Add relevant certifications.")

    # --------------------------------------
    # Resume Length
    # --------------------------------------

    words = len(resume_text.split())

    if 250 <= words <= 700:
        score += 15
    elif words < 250:
        comments.append("📄 Resume is too short.")
    else:
        comments.append("📄 Resume is too lengthy.")

    # --------------------------------------
    # General ATS Suggestions
    # --------------------------------------

    suggestions = [
        "❌ Avoid profile pictures.",
        "❌ Avoid colorful backgrounds.",
        "❌ Avoid tables and text boxes.",
        "❌ Avoid decorative icons.",
        "✅ Use simple fonts like Arial or Calibri.",
        "✅ Save your resume in PDF format.",
        "✅ Keep your resume to one page if possible.",
        "✅ Use clear section headings.",
        "✅ Quantify achievements wherever possible."
    ]

    comments.extend(suggestions)

    if score > 100:
        score = 100

    return score, comments