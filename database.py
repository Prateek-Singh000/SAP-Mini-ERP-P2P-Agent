from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import urllib.parse
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("HANA_USER", "DBADMIN")
DB_PASSWORD = urllib.parse.quote_plus(os.getenv("HANA_PASSWORD", "FallbackPassword"))
DB_HOST = os.getenv("HANA_HOST", "fallback-host")
DB_PORT = "443"

# The SAP driver strictly requires these flags as lowercase strings in the URL
DATABASE_URL = f"hana://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/?encrypt=true&sslValidateCertificate=false"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()