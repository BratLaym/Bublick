from dataclasses import dataclass

from environs import Env


@dataclass
class Config:
    db_path: str
    debug: bool


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)

    return Config(
        debug=env.bool("DEBUG", default=False),
        db_path=env("DB_PATH")
    )
