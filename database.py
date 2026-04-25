from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://taskuser:1234@172.17.0.1/taskdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
