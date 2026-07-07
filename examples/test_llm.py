from prompt_generator.llm import LLM

API_KEY = "YOUR_GROQ_API_KEY"

llm = LLM(API_KEY)

response = llm.generate(
    system_prompt="You are a helpful assistant",
    user_prompt="Introduce yourself in one sentence"
)

print(response)