import json
from pathlib import Path
from app.core.config import settings

FILE_PATH = Path(settings.DATA_FILE)
print("Reading from:", FILE_PATH.resolve())
def read_data():
    if not FILE_PATH.exists():
        return []
    with open(FILE_PATH, "r") as f:
        return json.load(f)

def write_data(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4,default=str)