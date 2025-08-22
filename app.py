from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/", response_class=HTMLResponse)
def read_index():
    with open("index.html") as f:
        return f.read()

@app.post("/ask")
def ask_agent(question: str = Form(...)):
    # Simple pre-programmed responses
    responses = {
        "email app": "To install an email app, go to your phone's app store (Google Play or Apple App Store), search for 'Gmail' or 'Outlook', and tap install.",
        "add account": "Open the email app, go to settings, select 'Add Account', and follow the prompts with your email and password.",
        "default": "Sorry, I don't have instructions for that yet."
    }

    # Simple keyword matching
    for key, answer in responses.items():
        if key.lower() in question.lower():
            return {"response": answer}

    return {"response": responses["default"]}≈
