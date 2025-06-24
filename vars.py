# Add your details here and then deploy by clicking on HEROKU Deploy button
from os import environ

API_ID = int(environ.get("API_ID", "27765349"))
API_HASH = environ.get("API_HASH", "9df1f705c8047ac0d723b29069a1332b")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Sudo Users Configuration
SUDO_USERS = list(map(int, environ.get("SUDO_USERS", "1116405290").split(","))) if environ.get("SUDO_USERS", "") else []

# Admin Configuration - Has FULL and PERMANENT access
ADMIN_USERS = list(map(int, environ.get("ADMIN_USERS", "1116405290").split(","))) if environ.get("ADMIN_USERS", "") else []
