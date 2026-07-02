from fastapi import FastAPI
from api.books import router as books_router

app = FastAPI()

app.include_router(router=books_router, prefix="/api/v1")