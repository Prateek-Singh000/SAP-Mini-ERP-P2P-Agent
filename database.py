from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import urllib.parse
import os
from dotenv import load_dotenv

load_dotenv()

# First, try to grab the full URL (This matches our Render deployment)
DATABASE_URL = os.getenv("SAP_DATABASE_URL")

# If no full URL is found, build it from individual parts (For local testing)
if not DATABASE_URL:
    DB_USER = os.getenv("HANA_USER", "DBADMIN")
    # quote_plus safely encodes passwords with special characters like '#'
    DB_PASSWORD = urllib.parse.quote_plus(os.getenv("HANA_PASSWORD", "FallbackPassword"))
    DB_HOST = os.getenv("HANA_HOST", "fallback-host")
    DB_PORT = "443"
    
    # Use hana+hdbcli for the SAP HANA SQLAlchemy dialect
    DATABASE_URL = f"hana+hdbcli://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/?encrypt=true&sslValidateCertificate=false"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()