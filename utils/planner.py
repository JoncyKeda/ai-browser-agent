import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def plan_task(task):
    prompt = f"""
    Break the following task into clear step-by-step actions:

    Task: {task}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an AI planning assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response['choices'][0]['message']['content']
