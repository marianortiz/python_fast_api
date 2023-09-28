from fastapi import FastAPI
from app.config.database import Base, engine
from app.api.user import router as user_router


Base.metadata.create_all(bind=engine)  # create all tables.


def create_app():
    app = FastAPI()

    app.include_router(user_router, prefix="/api")  # Inlcude User route.

    return app
