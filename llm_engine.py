import openai

def call_gpt(api_key, prompt, temperature=0.7):
    openai.api_key = api_key
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=1000
        )
    except openai.error.InvalidRequestError:
        # Fallback to GPT-3.5 if GPT-4 is not accessible
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=1000
        )
    return response['choices'][0]['message']['content'].strip()
