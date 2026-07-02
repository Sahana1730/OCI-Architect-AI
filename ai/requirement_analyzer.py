import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_requirements(project_description):

    prompt = f"""
You are a Senior Oracle Cloud Architect.

Analyze the following application.

Application Description:
{project_description}

Return ONLY valid JSON.

Use this exact schema:

{{
    "application": "",
    "traffic": "",
    "users": 0,

    "compute": {{
        "shape": "",
        "ocpu": 0,
        "memory": 0
    }},

    "database": {{
        "required": true,
        "storage": 0
    }},

    "object_storage": {{
        "required": true,
        "storage": 0
    }},

    "load_balancer": true,

    "bandwidth_tb": 0
}}

Rules:

- Return JSON only.
- No markdown.
- No explanation.
- Estimate realistic OCI resources.
"""

    response = model.generate_content(prompt)

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()

    elif text.startswith("```"):
        text = text.replace("```", "").strip()

    return json.loads(text)