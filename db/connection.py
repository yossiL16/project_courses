import mysql.connector
from soldier_courses_explorer.config import *
def get_connection():
    return mysql.connector.connect(
    host=DB_CONFIG["host"],
    user=DB_CONFIG["user"],
    password=DB_CONFIG["password"],
    database=DB_CONFIG["database"]
        )