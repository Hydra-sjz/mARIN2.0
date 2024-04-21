# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX


import json
import os


def get_user_list(config, key):
    with open("{}/Mikobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    # Configuration class for the bot

    # Enable or disable logging
    LOGGER = True

    # <================================================ REQUIRED ======================================================>
    # Telegram API configuration
    API_ID = 28124597  # Get this value from my.telegram.org/apps
    API_HASH = "7d71ada2c2b74ed53cc1b5ad829b5277"

    # Database configuration (PostgreSQL)
    DATABASE_URL = "postgres://yaemiko_user:joG3xtaeibSq1OhFFljhvEgWdxFMVs92@dpg-co6geesf7o1s73dit1kg-a.singapore-postgres.render.com/yaemiko"

    # Event logs chat ID and message dump chat ID
    EVENT_LOGS = -1001989832800
    MESSAGE_DUMP = -1001989832800

    # MongoDB configuration
    MONGO_DB_URI = "mongodb+srv://exp69:exp69@cluster0.kr93qbe.mongodb.net/?retryWrites=true&w=majority"

    # Support chat and support ID
    SUPPORT_CHAT = "indian_Support"
    SUPPORT_ID = -1001989832800

    # Database name
    DB_NAME = "Miko2DB"

    # Bot token
    TOKEN = "6308339365:AAF1CXluU8Jz3aNvA4h5M7slOa33eM_hTjs"  # Get bot token from @BotFather on Telegram

    # Owner's Telegram user ID (Must be an integer)
    OWNER_ID = 5907205317

    STRING_SESSION = getenv(
        "STRING_SESSION",
        "1BVtsOH8BuzEMQj67t22HjgBT1e30UnrffoSx5WfYB5xbNgQnGPbzicK06hUen6iN89rWeG2mv8-9wQ0mVRHiJheO-1Lczk6nJjh8qDOD9d5V5yokzLjQ40DoBVGKROr7JtzFrFBh1Q5y8P58wEV9bHBke6dH444IQRd0MNCswXLPDAk_k6ghvACZOCSOQWejJbEvNiY3YPa78e6KFjrFVxfXkiKB8Cl0Fn29unGJJ510xovR63tGkBJuwU6wzUnlNV_hW--LgWyP6FKBppYcnMV0OG40WePSjZ3NPeztv6McDMWWBL0zMOFDtJLeBLjyhfns7eYoqXAu1kkF7XgpqYt4KvfJ9i0=",
    )
    # <=======================================================================================================>

    # <================================================ OPTIONAL ======================================================>
    # Optional configuration fields

    # List of groups to blacklist
    BL_CHATS = []

    # User IDs of sudo users, dev users, support users, tiger users, and whitelist users
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    DEMONS = get_user_list("elevated_users.json", "supports")
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")

    # Toggle features
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True

    # Modules to load or exclude
    LOAD = []
    NO_LOAD = []

    # Global ban settings
    STRICT_GBAN = True
    BAN_STICKER = (
        "CAACAgUAAxkBAAEGWC5lloYv1tiI3-KPguoH5YX-RveWugACoQ4AAi4b2FQGdUhawbi91DQE"
    )

    # Temporary download directory
    TEMP_DOWNLOAD_DIRECTORY = "./"
    # <=======================================================================================================>


# <=======================================================================================================>


class Production(Config):
    # Production configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True


class Development(Config):
    # Development configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True
