import os
from dotenv import dotenv_values
import sqlalchemy

env_vars = dotenv_values(".env.example")

USERNAME = env_vars.get("USERNAME")
PASSWORD = env_vars.get("PASSWORD")
DB_HOSTNAME = env_vars.get("DB_HOSTNAME")
DB_NAME = env_vars.get("DB_NAME")

DATABASE_URI = f"postgresql://{USERNAME}:{PASSWORD}@{DB_HOSTNAME}/{DB_NAME}"
engine = sqlalchemy.create_engine(DATABASE_URI)
