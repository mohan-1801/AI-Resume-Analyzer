import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

def analyze_resume(text):

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    prompt = f"""
You are an expert ATS recruiter.

Analyze the resume professionally.

Output format:

Resume Score: <score out of 100>

Strengths:
- point 1
- point 2
- point 3

Weaknesses:
- point 1
- point 2
- point 3

Missing Important Elements:
- element 1
- element 2

Suggestions to Improve:
- suggestion 1
- suggestion 2
- suggestion 3

Resume:
{text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content