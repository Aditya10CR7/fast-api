from settings import settings

print("🚨 DEBUG: DATABASE_URL = ", repr(settings.DATABASE_URL)) 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from typing import Generator

engine = create_engine(settings.DATABASE_URL)  # This is what's breaking
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
