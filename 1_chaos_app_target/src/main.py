from fastapi import FastAPI

from dotenv import load_dotenv
load_dotenv()

from src.api import test

# app = FastAPI()
# app.include_router(hello_world.router)

def create_app():
    app = FastAPI()
    app.include_router(test.router)
    return app

app = create_app()

def main():
    ...
    
if __name__ == "__main__":
    main()
