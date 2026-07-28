import requests

from config import settings

class OllamaClient:

	def __init__(self):
		self.url = settings.OLLAMA_URL
		self.model = settings.DEFAULT_MODEL
		self.timeout = settings.REQUEST_TIMEOUT

	def generate(self, prompt: str) -> str:
		payload = {
			"model": self.model,
			"prompt": prompt,
			"stream": False
		}

		response = requests.post(
			self.url,
			json=payload,
			timeout=self.timeout
		)

		response.raise_for_status()
		
		data = response.json()

		return data["response"]

ollama = OllamaClient()
