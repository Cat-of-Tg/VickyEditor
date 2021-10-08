# By @TroJanzHEX


import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1994325746:AAEdE8sDfHmwX9345yhJMrPVOdb5CoIir7I")

    APP_ID = int(os.environ.get("APP_ID", 6826285))

    API_HASH = os.environ.get("API_HASH", "916b4b01a784cf5c192e00ffacb3fc89")

    # Get this api from https://www.remove.bg/b/background-removal-api
    RemoveBG_API = os.environ.get("RemoveBG_API", "o6fwphkpDUkREAg8NdAJCF2f")
