import os
import time
import streamlit as st
import google.generativeai as genai

# ==========================================
# LOAD GEMINI API KEY
# ==========================================

api_key = None

# Load from .env (Local)
try:
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
except Exception:
    pass

# Load from Streamlit Cloud Secrets
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

# Fast Gemini Model
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

1. Application Overview
2. Why each OCI service is selected
3. Security Recommendations
4. Scalability Recommendations
5. Best Practices

Keep the explanation beginner-friendly.

Maximum 200 words.
"""

    try:

        print("\n========== GEMINI PROMPT ==========")
        print(prompt)
        print("==================================")

        start = time.time()

        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                temperature=0.2,
                max_output_tokens=250,
            )
        )

        end = time.time()

        print(f"✅ Gemini Time: {end - start:.2f} seconds")

        if hasattr(response, "text") and response.text:
            return response.text

        if hasattr(response, "candidates"):
            try:
                return response.candidates[0].content.parts[0].text
            except Exception:
                pass

        return "No response generated."

    except Exception as e:

        print("Gemini Error:", str(e))

        return f"""
## ❌ Gemini Error

{str(e)}
"""