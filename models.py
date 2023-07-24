from sqlalchemy import Boolean, Column, Integer, String, Text

from database import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary=True)
    username = Column(String(25), unique=True)
    email = Column(String(80), unique=True)
    password = Column(Text, nullable=True)
    is_staff = Column(Boolean, default=False)
