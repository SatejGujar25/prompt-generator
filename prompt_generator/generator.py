import json

from .llm import LLM
from .craft import build_craft_prompt
from .scorer import build_score_prompt


class PromptGenerator:


    def __init__(self,
                api_key: str,
                title: str,
                context: str,
                difficulty: str = None,
                tone: str = None, 
                language: str = None,
                length: str = None
                ):
        
        self.title = title
        self.context = context
        self.difficulty = difficulty
        self.tone = tone
        self.language = language
        self.length = length

        self.prompt = None
        self.llm = LLM(api_key)

    def gen_prompt(self, n: int = 1):

            prompts = []

            for _ in range(n):
                system_prompt, user_prompt = build_craft_prompt(
                    self.title,
                    self.context,
                    self.difficulty,
                    self.tone,
                    self.language,
                    self.length
                )

                response = self.llm.generate(
                    system_prompt,
                    user_prompt
                )

                prompts.append(response)
            self.prompt = prompts

            return prompts

    def Score(self):
         if self.prompt == None:
              raise ValueError ("Generate Prompt Before generating Score")
         
         system_prompt, user_prompt = build_score_prompt(self.prompt[0])

         response = self.llm.generate(
              system_prompt, user_prompt
         )

         return json.loads(response)
