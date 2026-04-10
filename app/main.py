from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import cashback
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cashback API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # libera tudo (dev)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cashback.router)


