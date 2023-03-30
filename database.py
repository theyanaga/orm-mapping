from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from entities.entity_base import EntityBase
from env import getenv
# This file contains the database set up

def _engine_str(database=getenv("POSTGRES_DATABASE")) -> str:
    """Helper function for reading settings from environment variables to produce connection string."""
    dialect = "postgresql+psycopg2"
    user = getenv("POSTGRES_USER")
    password = getenv("POSTGRES_PASSWORD")
    host = getenv("POSTGRES_HOST")
    port = getenv("POSTGRES_PORT")
    return f"{dialect}://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(_engine_str(), echo=True)

# Dependency
def get_db():
    session = Session(engine)
    try: 
        yield session
    finally:
        session.close()

