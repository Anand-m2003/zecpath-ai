# Zecpath – Resume Section Detection Accuracy Report

## Dataset

Total resumes evaluated: 10

The evaluation uses the 10 labeled resume samples created for the Day 8 section segmentation task.

## Target Sections

The classifier evaluates the following sections:

- Education
- Work Experience
- Skills
- Certifications
- Projects

## Results

| Section | Correctly Detected | Total | Accuracy |
|---|---:|---:|---:|
| Education | 10 | 10 | 100% |
| Work Experience | 10 | 10 | 100% |
| Skills | 10 | 10 | 100% |
| Certifications | 10 | 10 | 100% |
| Projects | 10 | 10 | 100% |

## Overall Result

All five required resume sections were successfully detected across all 10 sample resumes.

Overall section detection accuracy: 100%

## Testing

The complete sample set was tested using the automated pytest test:

`tests/test_all_resume_sections.py`

Result:

`1 passed`

## Conclusion

The current rule-based section classifier successfully identifies the required resume sections in the available labeled sample resumes.