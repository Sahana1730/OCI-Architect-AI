import os
import streamlit as st
import google.generativeai as genai

# ==========================================
# LOAD API KEY
# ==========================================

api_key = None

# Load from .env (Local)
try:
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
except:
    pass

# Load from Streamlit Cloud Secrets
if not api_key:
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except:
        pass

if not api_key:
    raise Exception("GEMINI_API_KEY not found.")

# Configure Gemini
genai.configure(api_key=api_key)

# ==========================================
# FAST GEMINI MODEL
# ==========================================

model = genai.GenerativeModel("gemini-2.5-flash")

# ==========================================
# AI ARCHITECT
# ==========================================

def explain_architecture(user_input, services):

    prompt = f"""
You are an experienced Oracle Cloud Infrastructure (OCI) Architect.

Application Description:
{user_input}

Recommended OCI Services:
{', '.join(services)}

Explain the architecture using the following format:

## Application Overview
Briefly explain what the application does.

## Why These OCI Services?
Explain why each service is recommended.

## Security Recommendations
Mention IAM, encryption, VCN, backups and least privilege.

## Scalability Recommendations
Explain autoscaling, load balancing and storage scalability.

## Best Practices
Give 5 practical OCI best practices.

Keep the explanation beginner-friendly.
Limit the response to around 300 words.
"""

    try:

        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                temperature=0.3,
                max_output_tokens=500
            )
        )

        return response.text

    except Exception as e:

        return f"""
### ❌ Gemini Error

{str(e)}
"""