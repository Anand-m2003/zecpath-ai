# Zecpath – AI Storage Structure

## 1. Resumes

**Format:** PDF or DOCX

Stores the original resume uploaded by a candidate.

## 2. Parsed Profiles

**Format:** JSON

Stores structured information extracted from a resume, including candidate details, skills, education, and experience.

## 3. ATS Scores

**Format:** JSON

Stores the candidate's job-matching score and skill-matching results.

## 4. Screening Reports

**Format:** JSON

Stores screening responses, evaluation results, and screening scores.

## 5. Interview Results

**Format:** JSON

Stores interview responses, evaluation results, and interview scores.

## Data Relationships

Candidate ID links a resume to its parsed profile.

Candidate ID and Job ID link ATS scores, screening reports, and interview results to a specific job application.