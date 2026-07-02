import os
import streamlit as st
import google.generativeai as genai

# ==========================================
# LOAD GEMINI API KEY
# ==========================================

api_key = None

# Local (.env)
try:
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
except Exception:
    pass

# Streamlit Cloud Secrets
if not api_key:
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass

if not api_key:
    raise Exception("GEMINI_API_KEY not found.")

# ==========================================
# CONFIGURE GEMINI
# ==========================================

genai.configure(api_key=api_key)

# Fast model
model = genai.GenerativeModel("gemini-2.5-flash")

# ==========================================
# AI ARCHITECT
# ==========================================

def explain_architecture(user_input, services):

    prompt = f"""
You are an experienced Oracle Cloud Infrastructure (OCI) Solution Architect.

Application Description:
{user_input}

Recommended OCI Services:
{", ".join(services)}

Explain ONLY the following:

## Application Overview
Brief overview of the application.

## Why These OCI Services?
Explain why every OCI service is selected.

## Security Recommendations
Mention IAM, VCN, encryption, backups and least privilege.

## Scalability Recommendations
Mention autoscaling, load balancing and database scaling.

## Best Practices
Give 5 practical OCI best practices.

Keep the explanation simple.
Maximum 250 words.
"""

    try:

        print("========== GEMINI PROMPT ==========")
        print(prompt)
        print("==================================")

        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                temperature=0.2,
                max_output_tokens=250,
            )
        )

        if hasattr(response, "text") and response.text:
            return response.text

        # Fallback for empty text responses
        if hasattr(response, "candidates"):
            try:
                return response.candidates[0].content.parts[0].text
            except Exception:
                pass

        return "No response generated."

    except Exception as e:

        return f"""
## ❌ Gemini Error

{str(e)}
"""