# Zecpath AI – Job Description Parsing System

## Objective

The Job Description Parsing System converts raw employer job descriptions into structured, AI-readable job requirement profiles.

## Processing Workflow

Raw Job Description
        ↓
JD Text Normalization
        ↓
Role Extraction
        ↓
Experience Extraction
        ↓
Education Extraction
        ↓
Skill Extraction
        ↓
Skill & Role Normalization
        ↓
Preferred Skill Detection
        ↓
Responsibility Extraction
        ↓
Structured JD Profile
        ↓
JSON Output

## Components

### 1. JD Cleaner

File:

`parsers/jd_cleaner.py`

Responsibilities:

- Normalizes line endings
- Removes unwanted control characters
- Normalizes bullet symbols
- Removes excessive spaces
- Cleans individual lines

### 2. JD Synonym Mapping

File:

`parsers/jd_synonyms.py`

Responsibilities:

- Normalizes skill variations
- Normalizes job role variations
- Maps similar terms to a standard representation

Examples:

- `rest apis` → `REST API`
- `ml` → `Machine Learning`
- `python programmer` → `Python Developer`
- `back end developer` → `Backend Developer`

### 3. JD Parser

File:

`parsers/jd_parser.py`

Extracts:

- Job title
- Required skills
- Preferred skills
- Experience requirements
- Education requirements
- Responsibilities

### 4. Structured Output

The parsed information is stored as a JSON job profile.

Example output:

`data/jd_outputs/sample_python_developer_jd.json`

## AI-Friendly JD Profile

The structured profile follows the job description schema created for Zecpath AI.

It provides standardized information that can later be used by:

- ATS screening
- Candidate-job matching
- AI ranking
- Skill matching
- Experience evaluation
- Candidate scoring

## Current Approach

The current parser uses rule-based extraction and predefined synonym mappings.

This provides a predictable base parsing layer that can later be extended with NLP or LLM-based extraction.

## Sample Input

The sample JD is:

`data/test_job_descriptions/sample_python_developer_jd.txt`

## Sample Output

The structured JD profile is:

`data/jd_outputs/sample_python_developer_jd.json`