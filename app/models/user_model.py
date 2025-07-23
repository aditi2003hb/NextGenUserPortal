from sqlalchemy import Column, Integer, String
from app.database.connection import Base

class RegUser(Base):
    __tablename__ = "reg__users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    permanent_string_code = Column(String, nullable=False)
    state = Column(String, nullable=False)
    country = Column(String, nullable=False)
