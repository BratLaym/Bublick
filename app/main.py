from fastapi import FastAPI

from app.config import load_config
from app.db import create_table, get_score_db, save_change_score, save_user
from app.models import User, par_add_score, par_get_score


app = FastAPI()

config = load_config()

app.debug = config.debug

create_table()


@app.post('/add_user')
def get_user(user: User):
    save_user(user)
    return {"result": "successful"}


@app.post('/add_score')
def add_score(par: par_add_score):
    save_change_score(par.d_score, par.user_name)
    return {"result": "successful"}


@app.post('/get_score')
def get_score(par: par_get_score):
    score = get_score_db(par.user_name)
    return {"score": score}
