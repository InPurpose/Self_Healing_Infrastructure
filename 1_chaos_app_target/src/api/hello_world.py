from fastapi import APIRouter


router = APIRouter()
from src.services.hello_world_service import hello_world

@router.get("/hello_world")
def get_gmv():
    return hello_world()