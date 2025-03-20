import enum
import os
from typing import List

from sqlalchemy import Enum, ForeignKey, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
    sessionmaker,
)

engine = create_engine(
    os.environ["DATABASE_URL"]
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class BrickColour(enum.Enum):
    RED = "Red"
    BLUE = "Blue"
    GREEN = "Green"


class Tower(Base):
    __tablename__ = 'tower'

    id = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str]

    bricks: Mapped[List["Brick"]] = relationship(back_populates="tower")


class Brick(Base):
    __tablename__ = 'brick'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    colour: Mapped[enum.Enum] = Enum(BrickColour)
    length: Mapped[int]
    width: Mapped[int]
    tower_id: Mapped[int] = mapped_column(ForeignKey("tower.id"))

    tower: Mapped["Tower"] = relationship(back_populates="bricks")
