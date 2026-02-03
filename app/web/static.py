from fastapi.staticfiles import StaticFiles
from ..config import STATIC_DIR

def mount_static(app):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
