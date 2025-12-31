from fastapi import FastAPI
from pydantic import BaseModel
from agent import root_agent

app = FastAPI(title="ADK Agent API")

class Prompt(BaseModel):
    prompt: str

@app.get("/")
def health():
    return {"status": "alive"}

@app.post("/prompt")
def run_agent(data: Prompt):
    result = root_agent.run_live(data.prompt)
    return {"response": result}
