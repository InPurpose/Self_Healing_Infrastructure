from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from src.models.hero import HeroPublic, HeroCreate
from src.database.session import get_session

from src.services.test_service import hello_world,create_hero,get_all_heroes,get_hero_by_id

router = APIRouter()

@router.get("/hello_world")
def get_gmv():
    return hello_world()

@router.post("/heroes/", response_model=HeroPublic)
def create_hero(hero: HeroCreate, session:Session = Depends(get_session)):
    return create_hero(session=session,hero_data=hero)

@router.get("/heroes/", response_model=list[HeroPublic])
def read_heroes(session:Session = Depends(get_session)):
    return get_all_heroes(session=session)

@router.get("/heroes/{hero_id}", response_model=HeroPublic)
def read_hero(hero_id: int, session: Session = Depends(get_session)):
    hero = get_hero_by_id(session, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero