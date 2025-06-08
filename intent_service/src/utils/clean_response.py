def clean_response(response: str) -> str:
    response = response.replace("json", "")
    response = response.replace("```", "")
    response = response.replace("```", "")
    return response
