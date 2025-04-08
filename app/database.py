from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

os.makedirs("db",exist_ok=True)

DATABASE_URL =  ""

engine = create_engine( DATABASE_URL,connect_args={"check same thread": False} )
sessionLocal = sessionmaker(bind=engine, autoflush=False ,autocommit=False)
Base = declarative_base()
