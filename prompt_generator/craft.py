def build_craft_prompt(
        title: str,
        context: str,
        difficulty: str,
        tone: str,
        language: str,
        length: str
):
    system_prompt = """
        You are an expert AI Prompt Engineer with extensive experience in designing prompts for Large Language Models.

        Your task is to generate ONE professional prompt.

        Internally use the CRAFT framework:

        C - Context
        R - Role
        A - Action
        F - Format
        T - Task

        Important Instructions:

        • Use the Title as the primary objective.
        • Use the Context only to better understand the user's requirement.
        • Never change the user's intent.
        • Internally create all five CRAFT components.
        • DO NOT display headings like Context, Role, Action, Format or Task.
        • Merge all five components naturally into one well-written paragraph.
        • The final prompt should be ready to copy and use directly with any AI model.
        • Maintain the requested difficulty, tone, language and response length.
        • Return ONLY the final prompt.
    """

    user_prompt = f"""
        Title:
        {title}

        Context:
        {context}

        Difficulty:
        {difficulty}

        Tone:
        {tone}

        Language:
        {language}

        Length:
        {length}
    """
    return system_prompt, user_prompt

