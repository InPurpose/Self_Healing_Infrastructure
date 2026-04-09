from fastapi import FastAPI
from src.api import hello_world

from dotenv import load_dotenv
load_dotenv()

# app = FastAPI()
# app.include_router(hello_world.router)

def create_app():
    app = FastAPI()
    app.include_router(hello_world.router)
    return app

app = create_app()

def main():
    ...
    
if __name__ == "__main__":
    main()
