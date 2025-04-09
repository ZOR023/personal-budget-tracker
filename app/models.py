from sqlalchemy import Column, Integer, String, Float, Date
from .database import Base


class Transaction(Base):
  __tablename__ = "transaction"

  id = Column(Integer,primary_key=True)
  description = Column(String,nullable=False)
  amount = Column(Float,nullable=False)
  category = Column(String,nullable=False)
  date = Column(Date,nullable=False)