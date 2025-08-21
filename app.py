from fastapi import FastAPI
from pydantic import BaseModel
import subprocess
import os

app = FastAPI()

class Query(BaseModel):
    prompt: str

def run_ollama(prompt):
    process = subprocess.Popen(
        ["ollama", "run", "support-agent", prompt],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    output = ""
    for line in process.stdout:
        output += line
    process.wait()
    return output.strip()

@app.post("/ask")
def ask_agent(query: Query):
    try:
        response_text = run_ollama(query.prompt)
        if not response_text:
            response_text = "No response from Ollama agent."
        return {"response": response_text}
    except Exception as e:
        return {"response": f"Error running Ollama agent: {e}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
