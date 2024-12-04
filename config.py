from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "436b24700208cae55ded351d8f25fd7a")
      API_ID = int(getenv("API_ID", "17108931"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "7720043513:AAHdJwJ56zJ8Tinh_jeksqsEwPe-w8kbMlA")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002299241143:-1002478227330").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
