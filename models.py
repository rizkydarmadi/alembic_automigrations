from sqlalchemy import Boolean, Column, Integer, String
from db import Base


# define models


class User(Base):
    __tablename__ = "user"

    id = Column("id", Integer, primary_key=True, nullable=False)
    password = Column("password", String(length=128), nullable=False)
    new_password = Column("new_password", String(length=128), nullable=True)
    is_superuser = Column("is_superuser", Boolean, default=False, nullable=False)
    email = Column("email", String(length=128), nullable=False)
    nama = Column("nama", String(length=64))
