import backoff
from sqlalchemy.exc import OperationalError
from sqlmodel import SQLModel, create_engine

from core import config
from models import models


DB_URL = (f"postgresql://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@"
          f"{config.POSTGRES_HOST}:{config.POSTGRES_PORT}/{config.POSTGRES_DB}")

# SQLModel Engine
engine = create_engine(DB_URL)  # echo=True for debugging


# Deprecated
@backoff.on_exception(backoff.expo, OperationalError, max_time=5)
def init_db():
    SQLModel.metadata.create_all(engine)
