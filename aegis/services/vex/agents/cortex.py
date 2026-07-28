from ollama import ollama


class CortexAgent:

    name = "cortex"

    def __init__(self):
        self.system_prompt = """
Voce é Cortex, o núcleo de conversação do Aegis-Core.
Responda de forma clara e objetiva.
"""

    def chat(self, message: str) -> str:
        prompt = f"""
{self.system_prompt}

Usuário:
{message}

Cortex:
"""

        return ollama.generate(prompt)


cortex = CortexAgent()
