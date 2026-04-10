from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import cashback
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cashback API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
         "http://127.0.0.1:5500",
        "https://nology-1t.onrender.com",
        "https://nology-1.onrender.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cashback.router)


