from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import config
from database.database_model import LogModel


class LogDB(object):
    def __init__(self):
        HOST = config.database.host
        PORT = config.database.port
        NAME = config.database.name
        USER = config.database.user
        PASSWORD = config.database.password

        self.DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}"
        self.engine = create_engine(self.DATABASE_URL)
        self.SessionLocal = sessionmaker(bind=self.engine)

    def log(self, message) -> None:
        db = self.SessionLocal()
        try:
            log = LogModel(
                consume_id=message["unique_id"],
                dialog_id=message["dialog_id"],
                speaker=message['speaker'],
                content=message['content'],
                intent=message['intent'],
                segment=message['segment'],
                model_time=message['model_time'],
                timestamp=datetime.utcnow()
            )
            db.add(log)
            db.commit()
        except Exception as e:
            db.rollback()
        finally:
            db.close()

    def get_logs(self, unique_id: str):
        db = self.SessionLocal()
        try:
            logs = (
                db.query(LogModel)
                .filter(LogModel.consume_id == unique_id)
                .order_by(LogModel.timestamp.asc())
                .all()
            )
            return logs
        finally:
            db.close()
