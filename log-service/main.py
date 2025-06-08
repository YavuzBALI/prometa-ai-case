import uvicorn
from fastapi import FastAPI

from api import initialize_app
from config import config
from src.log_db_class import LogDB
app = FastAPI()
app.log_service = LogDB()

initialize_app(app)

if __name__ == '__main__':
    uvicorn.run(
        app,
        host='0.0.0.0',
        port=config.api.port
    )