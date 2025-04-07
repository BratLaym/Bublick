from uuid import UUID, uuid4
from pydantic import BaseModel


class User(BaseModel):
    id: UUID = uuid4()
    name: str
    score: int = 0


class par_get_score(BaseModel):
    user_name: str


class par_add_score(par_get_score):
    d_score: int
