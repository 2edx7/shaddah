from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse

from ..web.templates import templates
from ..services.diacritizer import DiacritizerService
from ..core.service_id import get_service_id
from ..config import HOST, PORT, SERVICE_NAME, SERVICE_SNID, VERSION

router = APIRouter()
diacritizer = DiacritizerService()


@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@router.post("/diacritize")
def diacritize(text: str = Form(...)):
    return {"result": diacritizer.diacritize(text)}


@router.get("/info")
def info():
    return {
        "service_id": get_service_id(),
        "snid": SERVICE_SNID,
        "name": SERVICE_NAME,
        "version": VERSION,
        "endpoint": "/diacritize",
        "host": HOST,
        "port": PORT,
    }
