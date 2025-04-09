from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

os.makedirs("db",exist_ok=True)

DATABASE_URL =  "sqlite:///db/budget.db"

engine = create_engine( DATABASE_URL,connect_args={"check_same_thread": False} )
SessionLocal = sessionmaker(bind=engine, autocommit=False,autoflush=False)
Base = declarative_base()
