import datetime
from sqlalchemy import Column, Integer, Float, String, DateTime, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class Client(Base):
    __tablename__ = 'Clients'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String, nullable=False)
    is_blocked = Column(Boolean, default=False)
    blocked_until = Column(DateTime)


class BankAccount(Base):
    __tablename__ = 'Bank_Accounts'
    id = Column(Integer, primary_key=True)
    balance = Column(Float)
    user_id = Column(Integer, ForeignKey(Client.id))
    user = relationship(Client, backref='bank_accounts')


class LoginAttempt(Base):
    FAILED_ATTEMPT = 'FAILED'
    SUCCESSFUL_ATTEMPT = 'SUCCESS'
    AFTER_BLOCK = 'AFTER BLOCK'

    __tablename__ = 'Login_Attempts'
    id = Column(Integer, primary_key=True)
    attempt_status = Column(String)
    attempt_timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    user_id = Column(Integer, ForeignKey(Client.id))
    user = relationship(Client, backref='login_attempts')

    def __str__(self):
        return "{} for user {}".format(self.attempt_status, self.user_id)

    def __repr__(self):
        return self.__str__()
