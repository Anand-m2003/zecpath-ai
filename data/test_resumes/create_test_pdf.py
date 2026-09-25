from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

output_file = "test_resume.pdf"

document = SimpleDocTemplate(
    output_file,
    pagesize=A4
)

styles = getSampleStyleSheet()
story = []

story.append(Paragraph("JOHN DOE", styles["Title"]))
story.append(Spacer(1, 12))

story.append(Paragraph("PROFESSIONAL SUMMARY", styles["Heading2"]))
story.append(
    Paragraph(
        "Python Developer with experience in Flask, Django, REST APIs and SQL.",
        styles["BodyText"]
    )
)
story.append(Spacer(1, 10))

story.append(Paragraph("TECHNICAL SKILLS", styles["Heading2"]))
story.append(
    Paragraph(
        "• Python<br/>"
        "• FLASK<br/>"
        "• Django<br/>"
        "• SQL<br/>"
        "• Git<br/>"
        "• REST API",
        styles["BodyText"]
    )
)
story.append(Spacer(1, 10))

story.append(Paragraph("EXPERIENCE", styles["Heading2"]))
story.append(
    Paragraph(
        "Python Developer - ABC Technologies<br/>"
        "2023 - 2025<br/>"
        "• Developed Flask-based web applications<br/>"
        "• Created REST APIs<br/>"
        "• Worked with SQL databases",
        styles["BodyText"]
    )
)
story.append(Spacer(1, 10))

story.append(Paragraph("EDUCATION", styles["Heading2"]))
story.append(
    Paragraph(
        "Bachelor of Computer Applications<br/>"
        "ABC University<br/>"
        "2023",
        styles["BodyText"]
    )
)
story.append(Spacer(1, 10))

story.append(Paragraph("PROJECTS", styles["Heading2"]))
story.append(
    Paragraph(
        "AI Resume Screening System<br/>"
        "Developed a system to extract and analyze resume information.<br/>"
        "Technologies: Python, Flask, NLP",
        styles["BodyText"]
    )
)
story.append(Spacer(1, 10))

story.append(Paragraph("CERTIFICATIONS", styles["Heading2"]))
story.append(
    Paragraph(
        "Python Programming Certification",
        styles["BodyText"]
    )
)

document.build(story)

print("PDF test resume created successfully.")