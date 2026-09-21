from google import genai
from google.genai import types
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def get_response(prompt):

    fixed_prompt = f"""
Answer the following question in valid HTML only.

Requirements:
- Use <h2>, <h3> headings.
- Use <p> for paragraphs.
- Use <ul><li> for bullet points.
- Use <pre><code> for code.
- Do not use Markdown.
- Do not include <html>, <body>, or <head> tags.

Question:
{prompt}
"""

    response = client.models.generate_content(
        model="models/gemini-3.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=fixed_prompt,
            temperature=0,
            max_output_tokens=500
        )
    )

    return response.text