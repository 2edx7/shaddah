from .paths import base_dir

HOST = "127.0.0.1"
PORT = 54166
URL = f"http://{HOST}:{PORT}"

BASE_DIR = base_dir()
STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "templates"

SERVICE_NAME = "Arabic Diacritizer"
SERVICE_SNID = "shaddah"
VERSION = "1.0.0"
