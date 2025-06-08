import json
import time

import google.generativeai as genai

from src.prompt.intent_analyze_prompt import prompt_intent_analyze
from src.utils.clean_response import clean_response


def analyze_intent_content(model: genai.GenerativeModel, content: str) -> dict:
    start = time.time()
    intent_analyze = {"content": content}
    response = model.generate_content(prompt_intent_analyze(content=content))
    response_string = response.text.strip()
    response_string = clean_response(response_string)
    response_json = json.loads(response_string)
    intent_analyze["intent"] = response_json["intent"]
    intent_analyze["segment"] = response_json["segment"]
    end = time.time()
    intent_analyze["model_time"] = end - start
    return intent_analyze
