from prompt_generator import PromptGenerator

API_KEY = "YOUR_GROQ_API_KEY"

pg = PromptGenerator(
    api_key = API_KEY,
    title="AI Resume Builder",
    context="Generate ATS scanner Resume Prompt",
    difficulty="Intermediate",
    tone="Professional",
    language="English",
    length="Medium"
)

prompt = pg.gen_prompt(1)
res = pg.Score()

print(res["score"])