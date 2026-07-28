from fastapi import FastAPI
import requests

app = FastAPI(title="Vex Control")

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"

@app.get("/status")
def status():
	return {
		"service":"Vex",
		"status": "online"
	}

@app.post("/ask")
def ask(prompt: str):
	response = requests.post(
		OLLAMA_URL,
		json={
		"model": "llama3.2:3b",
		"prompt": prompt,
		"stream": False
		}
	)

	return response.json()


