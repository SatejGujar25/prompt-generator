from groq import Groq

class LLM:
    # Handles all communication of GROQ API

    # constructor
    def __init__(self, api_key: str):
        # Intialize Groq Client

        self.client = Groq(api_key = api_key)
    

    def generate(self, system_prompt: str, user_prompt: str) -> str:

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
            {
                "role" : "system",
                "content" : system_prompt
            },

            {
                "role" : "user",
                "content" : user_prompt
            }
        ])

        return response.choices[0].message.content