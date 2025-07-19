from llm_engine import call_gpt

def generate_quiz(api_key, topic):
    prompt = (
        f"Generate 3 multiple choice questions with 4 options each (A, B, C, D) "
        f"for the topic: {topic}. Mark the correct answer with a star (*)."
    )
    content = call_gpt(api_key, prompt)
    questions = []

    blocks = content.split("\n\n")
    for block in blocks:
        lines = block.strip().split("\n")
        if len(lines) >= 5:
            question = lines[0]
            options = [line.replace('*', '').strip() for line in lines[1:5]]
            questions.append({"question": question, "options": options})
    return questions
