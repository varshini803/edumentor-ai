import openai

def call_gpt(api_key, prompt, temperature=0.7):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=1000
    )
    return response['choices'][0]['message']['content'].strip()

def explain_topic(api_key, topic, level):
    prompt = f"Explain the topic '{topic}' at a {level.lower()} level."
    return call_gpt(api_key, prompt)
