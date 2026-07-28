from agents.cortex import cortex

class Router:
	def chat(self, message: str) -> str:
		return cortex.chat(message)

router = Router()
