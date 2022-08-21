from sqlalchemy import create_engine

from db.db import DB_URL


# SQLAlchemy Engine
engine = create_engine(DB_URL)
