from sqlalchemy import Column, String, Integer
from app.config.database import Base


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, autoincrement=True, unique=True)
    username = Column(String(255), primary_key=True,
                      nullable=False, unique=True)
    user_password = Column(String(255), nullable=False)
    user_email = Column(String(255), nullable=False)
    user_firstname = Column(String(255), nullable=False)
    user_lastname = Column(String(255), nullable=False)

    def __init__(self, username, user_password, user_email, user_firstname, user_lastname):
        self.username = username
        self.user_password = user_password
        self.user_email = user_email
        self.user_firstname = user_firstname
        self.user_lastname = user_lastname

    def to_Json(self):
        return {
            'username': self.username,
            'user_email': self.user_email,
            'user_firstname': self.user_firstname,
            'user_lastname': self.user_lastname
        }
