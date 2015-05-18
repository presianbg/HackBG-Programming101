from base import Base
from AAA_controller import AuthenticationController

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class BankController:

    def __init__(self, db_conn_string, block_afer_n_logins=5, block_for_n_minutes=5):
        self.__engine = create_engine(db_conn_string)
        Base.metadata.create_all(self.__engine)

        self.__session = Session(bind=self.__engine)
        self.__authaa = AuthenticationController(self.__session, block_afer_n_logins, block_for_n_minutes)

    def __commit_changes(self, objects):
        self.__session.add_all(objects)
        self.__session.commit()

    def register(self, username, password):
        return self.__authaa.register(username, password)

    def login(self, username, password):
        return self.__authaa.login(username, password)

    def change_password(self, client, password):
        return self.__authaa.change_password(client, password)
