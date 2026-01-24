from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg://user:password@localhost:5432/tickets_db"

engine = create_engine(DATABASE_URL, echo=True)

session_local = sessionmaker(bind=engine, autocommit=False, autoflush=False)
