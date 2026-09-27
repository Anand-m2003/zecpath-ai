import json
from pathlib import Path

from parsers.jd_parser import build_job_profile


input_file = Path(
    "data/test_job_descriptions/sample_python_developer_jd.txt"
)

output_dir = Path("data/jd_outputs")
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / "sample_python_developer_jd.json"


raw_text = input_file.read_text(encoding="utf-8")

job_profile = build_job_profile(raw_text)

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(job_profile, file, indent=4, ensure_ascii=False)


print(f"JD profile generated successfully: {output_file}")