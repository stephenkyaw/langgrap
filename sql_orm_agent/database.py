from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

# Database setup
DATABASE_URL = "sqlite:///example.db"
engine = create_engine(DATABASE_URL)
metadata = MetaData()
metadata.reflect(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
