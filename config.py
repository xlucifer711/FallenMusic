from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph//file/835b48f330763bffc34a7.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph//file/835b48f330763bffc34a7.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/SORS0Coo")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/S_EG_P")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1355571767").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
