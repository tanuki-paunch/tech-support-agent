from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Serve static files (if you add CSS/JS)
app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/", response_class=HTMLResponse)
def read_index():
    """Serve index.html at the root URL"""
    with open("index.html") as f:
        return f.read()

@app.post("/ask")
async def ask_agent(request: Request):
    """Endpoint to handle chat prompts"""
    data = await request.json()
    prompt = data.get("prompt", "")
    # Simple canned response or echo back the prompt
    response_text = f"You asked: {prompt}. Here's a sample response."
    return JSONResponse({"response": response_text})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
