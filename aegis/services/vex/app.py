from fastapi import FastAPI
from models import ChatRequest, ChatResponse
from router import router

app = FastAPI(
	title="Aegis Vex",
	version="0.1.0"
)

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
	response = router.chat(request.message)
	
	return ChatResponse(
		response=response
	)
