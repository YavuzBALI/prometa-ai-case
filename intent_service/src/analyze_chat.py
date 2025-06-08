from typing import Optional

import google.generativeai as genai

from config import config
from src.utils.ask_llm import analyze_intent_content
from src.utils.logging import log_info


class AnalyzeChat(object):
    def __init__(self):
        genai.configure(api_key=config.gemini.api_key)
        self.model = genai.GenerativeModel(config.gemini.model_name)

        self.dialog_id: Optional[str] = None
        self.unique_id: Optional[str] = None

    def analyze(self, chat: dict, unique_id: str) -> None:
        self.dialog_id = chat["dialog_id"]
        for message in chat["utterances"]:
            analyze_result = {"unique_id": unique_id, "dialog_id": self.dialog_id}
            if message["speaker"] == "agent":
                analyze_result['speaker'] = message["speaker"]
                analyze_result["content"] = message["text"]
                analyze_result["intent"] = ""
                analyze_result["segment"] = ""
                analyze_result['model_time'] = 0.0

            else:
                analyze_result['speaker'] = message["speaker"]
                intent_analyze = analyze_intent_content(self.model, message["text"])
                analyze_result.update(intent_analyze)
            log_info(analyze_result)

        analyze_result = {"unique_id": unique_id, "dialog_id": self.dialog_id, "speaker": "agent", "content": "END",
                          "intent": "END", "segment": "END", "model_time": 0.0}
        log_info(analyze_result)
