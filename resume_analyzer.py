from pypdf import PdfReader

reader = PdfReader("MY RESUME.pdf")

text = ""

for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
        text += page_text

required_skills = [
    "Python",
    "SQL",
    "Machine Learning",
    "Deep Learning",
    "AI",
    "Git",
    "LangChain"
]

found_skills = []
missing_skills = []

for skill in required_skills:
    if skill.lower() in text.lower():
        found_skills.append(skill)
    else:
        missing_skills.append(skill)

score = int((len(found_skills) / len(required_skills)) * 100)

print("\n===== AI ENGINEER REPORT =====")
print(f"\nResume Score: {score}/100")

print("\nSkills Found:")
for skill in found_skills:
    print("✓", skill)

print("\nMissing Skills:")
for skill in missing_skills:
    print("✗", skill)