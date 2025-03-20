import enum
import os
from typing import List

from sqlalchemy import Column, Enum, ForeignKey, Integer, MetaData, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

class BrickColour(enum.Enum):
    red = 1
    blue = 2
    green = 3
meta = MetaData()

class Tower(Base):
    __tablename__ = 'tower'
    metadata = meta
    id = mapped_column(Integer, primary_key=True)

    bricks: Mapped[List["Brick"]] = relationship(back_populates="tower")

class Brick(Base):
    __tablename__ = 'brick'
    metadata = meta
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    colour: Mapped[enum.Enum] = Enum(BrickColour)
    size: Mapped[int]
    tower_id: Mapped["Tower"] = mapped_column(ForeignKey("tower.id"))

    tower: Mapped["Tower"] = relationship(back_populates="bricks")

engine = create_engine(
    os.environ["DATABASE_URL"]
)


meta.create_all(engine)



# tower = Table(
#     "tower",
#     meta,
#     Column("id", Integer, primary_key=True)
# )
# tower.create(engine)

# brick = Table(
#     "brick",
#     meta,
#     Column("id", Integer, primary_key=True),
#     Column("colour", Enum(BrickColour)),
#     Column("size", Integer),

# )
# brick.create(engine)

# brick_tower = Table(
#     "tower_brick",
#     meta,
#     Column("id", primary_key=True)
#     Column("tower_id", ForeignKey("tower.id")),
#     Column("brick_id", ForeignKey("brick.id"))
# )
# brick_tower.create(engine)
