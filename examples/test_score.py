from prompt_generator.scorer import build_score_prompt
from prompt_generator.llm import LLM

API_KEY = "YOUR_GROQ_API_KEY"

llm = LLM(API_KEY)

prompt = """
Create a comprehensive resume for a mid-level professional, assuming the role of a career counselor, and provide a tailored action plan to enhance the candidate's 
job prospects by incorporating relevant keywords and phrases that can effectively pass through an Applicant Tracking System (ATS) scanner. The resume should be formatted in a clean and concise manner, using a standard font and bullet points to highlight key skills, experience, and achievements,
while maintaining a length of approximately 1-2 pages. The task is to design a well-structured resume that not only showcases the candidate's qualifications and expertise but also demonstrates their value proposition as a potential employee, 
ensuring a high ranking in the ATS scanner and increasing the chances of being noticed by the hiring manager.
"""

system_prompt , user_prompt = build_score_prompt(prompt)

response = llm.generate(
    system_prompt,
    user_prompt
)

