import os
import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from models import ChatRequest, ChatResponse
from router import router

app = FastAPI(
	title="Aegis Vex",
	version="0.1.0"
)

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)


static_dir = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_dir):
	app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/", response_class=FileResponse)
def read_root():
	index_file = os.path.join(static_dir, "index.html")
	return FileResponse(index_file)

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

