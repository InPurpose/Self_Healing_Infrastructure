from sqlmodel import Session, select
from src.models import Hero, HeroCreate

def hello_world() -> str :
    return "Hello World!"


def create_hero(session: Session, hero_data: HeroCreate) -> Hero:
    db_hero = Hero.model_validate(hero_data)
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero

def get_all_heroes(session: Session) -> list[Hero]:
    return session.exec(select(Hero)).all()

def get_hero_by_id(session: Session, hero_id: int) -> Hero | None:
    return session.get(Hero, hero_id)