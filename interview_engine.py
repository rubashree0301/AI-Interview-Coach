from config import model

def generate_question():
    
    prompt = "Generate one technical interview question for a software developer."

    response = model.generate_content(prompt)

    return response.text