import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    AUTH_USERS = int(os.environ.get("AUTH_USERS", ""))