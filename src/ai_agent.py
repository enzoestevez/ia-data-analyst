# ai_agent.py

import os
from openai import OpenAI


def ask_ai_about_dataset(context, question):
    """
    Sends dataset context and a user question to the OpenAI model
    to generate analytical insights.
    """

    api_key = os.getenv("OPENAI_API_KEY")

    # Si no hay API key configurada
    if not api_key:
        return (
            "⚠️ OpenAI API key not found.\n"
            "Set the environment variable OPENAI_API_KEY to enable AI insights."
        )

    try:
        client = OpenAI(api_key=api_key)

        prompt = f"""
You are a professional Data Analyst.

Use the dataset description below to answer the user's question.

DATASET CONTEXT:
{context}

USER QUESTION:
{question}

Provide:
- Analytical insights
- Observations about patterns
- Suggestions for possible visualizations
"""

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error calling OpenAI API: {e}"