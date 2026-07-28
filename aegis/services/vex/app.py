import time
from fastapi import FastAPI
from models import ChatRequest, ChatResponse
from router import router

app = FastAPI(
	title="Aegis Vex",
	version="0.1.0"
)

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
	start_time = time.time()
	response = router.chat(request.message)
	elapsed = round(time.time() - start_time, 2)
	
	return ChatResponse(
		agent="cortex",
		status="success",
		response=response,
		execution_time=elapsed
	)

