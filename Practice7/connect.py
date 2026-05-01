import psycopg2
from config import config


def connect_db():
    try:
        connection = psycopg2.connect(
            host=config["host"],
            database=config["database"],
            user=config["user"],
            password=config["password"],
            port=config["port"]
        )

        print("Connected successfully")
        return connection

    except Exception as e:
        print("Connection error:", e)
        return None