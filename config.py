import os

class Config(object):

    # get a token from @BotFather
    TG_BOT_TOKEN = "5700920410:AAEk8j5NZb6wiIVuu3-NS6AL243bl57EpvU"

    # The Telegram API things
    APP_ID = "4a05481a5da2d66f801acffc4ca5ee4b"
    API_HASH = 17945796
    # Get these values from my.telegram.org

    # Ban Unwanted Members..
    BANNED_USERS = []

    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 2097152000

    # chunk size that should be used with requests
    CHUNK_SIZE = 128

    # Database url
    DB_URI = "mongodb+srv://manu911:manu911@cluster0.frtlbqt.mongodb.net/?retryWrites=true&w=majority"

