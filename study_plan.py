from llm_engine import call_gpt

def create_study_plan(api_key, subject, days):
    prompt = (
        f"Create a detailed and realistic day-wise study plan for the subject '{subject}' "
        f"to be completed in {days} days. Include what to cover each day."
    )
    return call_gpt(api_key, prompt)
