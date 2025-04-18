import os
from dotenv import load_dotenv

load_dotenv()

config = {
    "GOOGLE_API_KEY" : os.getenv("GOOGLE_API_KEY"),
    "MYSQL": {
        "host": os.getenv("MYSQL_HOST"),
        "user": os.getenv("MYSQL_USER"),
        "password": os.getenv("MYSQL_PASSWORD"),
        "database": os.getenv("MYSQL_DATABASE"),
    }
}