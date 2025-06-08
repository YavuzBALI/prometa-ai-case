import datetime

from sqlalchemy import create_engine, Column, Float, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

from config import config

Base = declarative_base()


class LogModel(Base):
    __tablename__ = "model_log"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    consume_id= Column(String, nullable=False)
    dialog_id = Column(String, nullable=False)
    speaker = Column(String)
    content = Column(String)
    intent = Column(String)
    segment = Column(String)
    model_time = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)


def init_db():
    HOST = config.database.host
    PORT = config.database.port
    NAME = config.database.name
    USER = config.database.user
    PASSWORD = config.database.password

    DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}"

    engine = create_engine(DATABASE_URL)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
