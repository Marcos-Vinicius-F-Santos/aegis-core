from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
	message: str = Field(..., min_length=1, description="Mensagem enviada ao Aegis")

class ChatResponse(BaseModel):
	agent: str = Field(..., min_length=1, description="Mensagem enviada ao Aegis")	
	status: str = Field(..., min_length=1, description="Status da execucao")
	response: str = Field(..., min_length=1, description="Resposta gerada pelo agente")
	execution_time: float | None = Field(
		default=None,
		description="Tempo de execucao em segundos"
	)
