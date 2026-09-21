from contextlib import asynccontextmanager

from fastapi import FastAPI

from . import models  # noqa: F401
from .db import Base, engine
from .routers import emails, users


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="Secure Mail Backend Prototype", lifespan=lifespan)

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(emails.router, prefix="/emails", tags=["emails"])


@app.get("/health")
def health():
    return {"status": "ok"}
