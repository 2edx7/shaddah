import json
import uuid
from ..paths import base_dir

CONFIG_FILE = base_dir() / "service_config.json"


def get_service_id() -> str:
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)["service_id"]

    service_id = str(uuid.uuid4())
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump({"service_id": service_id}, f, indent=2)

    return service_id
