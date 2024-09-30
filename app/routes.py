from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.config import Settings

settings = Settings()
templates = Jinja2Templates(directory="app/templates/")

router = APIRouter()


@router.get("/")
def index(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})
