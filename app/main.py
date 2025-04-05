from fastapi import FastAPI

from app.config import load_config


app = FastAPI()

config = load_config()

app.debug = config.debug
