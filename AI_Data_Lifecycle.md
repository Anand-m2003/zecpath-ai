# Zecpath – AI Data Lifecycle

## 1. Resume Upload

The candidate uploads a resume in PDF or DOCX format.

The original resume is stored as raw resume data.

## 2. Resume Text Extraction

The resume extraction engine extracts text from the uploaded resume.

The extracted text is cleaned and normalized.

## 3. Profile Parsing

The cleaned resume text is converted into a structured candidate profile.

The profile contains information such as:
- Candidate details
- Skills
- Education
- Experience
- Certifications
- Projects

## 4. Job Description Processing

The employer's job description is normalized and converted into a structured job profile.

The profile contains:
- Job title
- Required skills
- Preferred skills
- Experience requirements
- Education requirements
- Responsibilities

## 5. ATS Evaluation

The candidate profile is compared with the job profile.

The system generates an ATS score and matching information.

## 6. AI Screening

Shortlisted candidates proceed to AI screening.

Screening responses and evaluation results are stored as screening reports.

## 7. AI Interview

Candidates proceed through the required interview stages.

Interview responses, evaluation results, and scores are stored as interview results.

## 8. Hiring Decision

The results from the hiring stages are used as inputs for the final hiring decision.

The decision data is associated with the Candidate ID and Job ID.

## Data Flow

Resume Upload
→ Text Extraction
→ Candidate Profile
→ Job Profile Matching
→ ATS Evaluation
→ AI Screening
→ AI Interview
→ Hiring Decision