# Zecpath – AI Metadata Standards

## 1. Candidate ID

**Purpose:** Uniquely identifies a candidate across the Zecpath platform.

**Example:**
CAND-0001

Used to connect:
- Resume
- Parsed profile
- ATS score
- Screening report
- Interview results

## 2. Job ID

**Purpose:** Uniquely identifies a job posted by an employer.

**Example:**
JOB-0001

Used to connect candidate evaluation data to a specific job.

## 3. Model Version

**Purpose:** Identifies the AI model or processing version used to generate an AI result.

**Example:**
ATS-v1.0

Used to track which model version generated:
- ATS scores
- Screening results
- Interview results

## 4. Timestamp

**Purpose:** Records when an AI processing event or result was created.

**Format:**
ISO 8601

**Example:**
2026-09-27T19:45:00+05:30

Used to track the chronological lifecycle of AI data.