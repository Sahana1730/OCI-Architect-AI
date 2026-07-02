import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env file
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")


def explain_architecture(user_input, services):

    prompt = f"""
You are a Senior Oracle Cloud Architect.

Application Description:

{user_input}

Recommended OCI Services:

{', '.join(services)}

Explain:

1. Why each OCI service was selected.
2. Security recommendations.
3. Scalability recommendations.
4. Best practices.

Keep the explanation simple for a Computer Science fresher.
"""

    response = model.generate_content(prompt)

    return response.text