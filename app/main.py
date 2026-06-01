from fastapi import FastAPI
from app.views.student_view import router

app = FastAPI()

app.include_router(router)