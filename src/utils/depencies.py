from pathlib import Path

from jinja2 import FileSystemLoader, Environment
from starlette.templating import Jinja2Templates

from src.db.database import SessionLocal

SRC_DIR = Path(__file__).resolve().parent.parent


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


loader = FileSystemLoader(
    SRC_DIR / 'templates'
)
env = Environment(loader=loader)
templates = Jinja2Templates(directory='/src/templates')
