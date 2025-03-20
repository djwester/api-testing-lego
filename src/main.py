import os
from dataclasses import dataclass

from database.database import Brick as BrickDB
from database.database import BrickColour
from database.database import Tower as TowerDB
from fastapi import FastAPI
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    os.environ["DATABASE_URL"]
)

Session = sessionmaker(bind=engine)
session = Session()


app = FastAPI()


@dataclass
class Brick:
    length: int
    width: int
    colour: BrickColour
    id: int | None = None


@dataclass
class Tower:
    title: str
    bricks: list[Brick]
    id: int | None = None


@app.get('/')
def root():
    return {"welcome to the app!"}


# Get Lego Tower
@app.get("/towers/{tower_id}/brick")
def get_top_brick(tower_id: int):
    # try:
    #     tower_info = data[tower_id]
    # except:
    #     return {f"Tower not found"}

    # num_bricks = tower_info["num_bricks"]

    # num_bricks = tower_info["num_bricks"]
    # return {f"Tower {tower_id} has {num} {colour} brick"}
    pass


# def write_to_db(data):
#     print(data)
#     t1 = TowerDB(id=1, bricks=data)

#     session.add(t1)
#     session.commit()


@app.post("/towers")
def create_tower(tower: Tower) -> dict:
    tower = TowerDB(
        title=tower.title,
        bricks=[]
    )

    session.add(tower)
    session.commit()

    return {"id": tower.id, "title": tower.title}


@app.get("/towers")
def towers():
    stmt = select(TowerDB)
    result = session.scalars(stmt).all()

    towers = []
    for row in result:
        tower = {"id": row.id, "title": row.title}
        towers.append(tower)

    return towers


@app.post("/towers/{tower_id}/brick")
def add_to_tower(item):
    return item


@app.put("/towers/{tower_id}/brick")
def replace_top_brick(item):
    return item


@app.delete("/towers/{tower_id}/brick")
def delete_top_brick(tower_id: int):
    pass
