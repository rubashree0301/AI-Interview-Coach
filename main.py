from fastapi import FastAPI
from interview_engine import generate_question

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Interview Coach Running"}

@app.get("/question")
def get_question():
    question = generate_question()
    return {"question": question}