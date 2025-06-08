def prompt_intent_analyze(content: str) -> str:
    PROMPT = f"""
        Analyze the sentence below:
        Sentence: "{content}"
    
        The output just  should be in this format:
        {{
        intent: "<inquiry/purchase_intent/complaint/greeting/plan_change/renewal/other>",
        segment: "<positive/neutral/negative>"
        }}
        """
    return PROMPT
