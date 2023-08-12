from fastapi import FastAPI

from .pastes.router import router as pastes_router

app = FastAPI()
app.include_router(pastes_router)


# @app.on_event("startup")
# def on_startup():
#     create_db_and_tables()


@app.get("/")
def home():
    return "Hello, World!"
