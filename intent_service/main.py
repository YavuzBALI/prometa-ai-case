import uvicorn
from fastapi import FastAPI

from api import initialize_api
from config import config
from src.analyze_chat import AnalyzeChat

app = FastAPI()

app.analyze_chat = AnalyzeChat()

initialize_api(app)


if __name__ == '__main__':
    uvicorn.run(
        app,
        host='0.0.0.0',
        port=config.api.port
    )