from sqlite3 import OperationalError, connect

from app.config import load_config
from app.models import User
from app.logging import logger


def create_table():
    config = load_config()

    con = connect(config.db_path)
    cur = con.cursor()

    try:
        cur.execute(
            """CREATE TABLE users
            (
                id VARCHAR(255) UNIQUE NOT NULL,
                name VARCHAR(255) UNIQUE NOT NULL,
                score INTEGER,
                PRIMARY KEY ( id )
            )
            """
        )
    except OperationalError:
        logger.info("tebletable users already exists")

    con.commit()
    con.close()


def save_user(user: User):
    config = load_config()

    con = connect(config.db_path)
    cur = con.cursor()

    cur.execute(
        "INSERT INTO users (id, name, score) VALUES (?, ?, ?)",
        (str(user.id), user.name, user.score)
    )

    con.commit()
    con.close()


def get_score_db(user_name: str):
    config = load_config()

    con = connect(config.db_path)
    cur = con.cursor()

    score = cur.execute(
        "SELECT (score) FROM users WHERE name = ?",
        (user_name, )
    ).fetchone()[0]

    con.commit()
    con.close()

    return score


def save_change_score(d_score: int, user_name: str):
    config = load_config()

    con = connect(config.db_path)
    cur = con.cursor()

    old_score = cur.execute(
        "SELECT (score) FROM users WHERE name = ?",
        (user_name, )
    ).fetchone()[0]

    logger.debug(old_score)

    cur.execute(
        "UPDATE users SET score = ? WHERE name = ?",
        (old_score + d_score, user_name)
    )

    con.commit()
    con.close()
