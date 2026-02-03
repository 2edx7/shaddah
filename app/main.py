import threading
import time
import webbrowser
import uvicorn
from fastapi import FastAPI

from .config import HOST, PORT, URL
from .api.routes import router
from .web.static import mount_static


def create_app() -> FastAPI:
    app = FastAPI(title="Shaddah")
    mount_static(app)
    app.include_router(router)
    return app


def open_browser():
    time.sleep(1.5)
    webbrowser.open(URL)


def run():
    app = create_app()
    threading.Thread(target=open_browser, daemon=True).start()
    uvicorn.run(
        app,
        host=HOST,
        port=PORT,
    )
