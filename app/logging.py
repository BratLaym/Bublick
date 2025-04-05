import logging


def setup_logger() -> logging.Logger:
    logger = logging.getLogger("Bublick")
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "[%(asctime)s] #%(levelname)-8s %(filename)s:"
        "%(lineno)d - %(name)s - %(message)s"
    )
    ch.setFormatter(formatter)

    logger.addHandler(ch)

    return logger


logger = setup_logger()
