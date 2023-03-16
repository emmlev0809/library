from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, validates
import re

# Base is called an Abstract Base Class - our SQL Alchemy models will inherit from this class
Base = declarative_base()



# Create an email database class
class EmailAddress(Base):
    __tablename__ = 'email'

    email_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    @validates('email')
    def validate_email(self, key, address):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(pattern, address):
            raise ValueError('Invalid email address')
        if key != 'email':
            raise ValueError('Key must be "email"')
        return address

    @validates('password')
    def validate_password(self, key, passw):
        pattern = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
        if not re.fullmatch(pattern, passw):
            raise ValueError('Invalid password')
        if key != 'password':
            raise ValueError('Key must be "email"')
        return passw

    def __repr__(self):
        return f"EmailAddress({self.email})"

