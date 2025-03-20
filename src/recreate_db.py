import os

from database.tower import Base
from sqlalchemy import MetaData, create_engine, engine

engine = create_engine(
    os.environ["DATABASE_URL"]
)

# meta = MetaData()
Base.metadata.create_all(engine)
