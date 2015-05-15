import sqlite3
from Client import Client
import os
from pass_check_and_prepare import PasswdCheckHash


class DataBankManager:

    GET_LOGIN = '''SELECT id, username, balance, message
        FROM clients
        WHERE username = ? AND password = ?
        LIMIT 1
        '''

    GET_HASH = '''SELECT password FROM clients WHERE username = ? LIMIT 1'''

    MAKE_ACC = '''INSERT INTO clients
        (username, password) values (?, ?)'''

    CHANGE_PASS = '''UPDATE clients SET password = ? WHERE id = ? '''

    def __init__(self, conn):
        self.conn = conn
        self.conn.row_factory = sqlite3.Row

    @classmethod
    def create_db_sql(cls, struct_file, db_name, create_if_exists=False):

        if not os.path.exists(db_name) or create_if_exists:
            conn = sqlite3.connect(db_name)
            cursor = conn.cursor()
            with open(struct_file, "r") as f:
                cursor.executescript(f.read())
            conn.commit()

            return DataBankManager(conn)

        conn = sqlite3.connect(db_name)
        return DataBankManager(conn)

    def register(self, username, password):
        cursor = self.conn.cursor()
        hashpassw = PasswdCheckHash.hash_password(password)
        try:
            cursor.execute(self.__class__.MAKE_ACC, (username, hashpassw))
            self.conn.commit()
        except Exception:
            return False

        if self.login(username, password):
            return True

        return False

    def login(self, username, password):
        cursor = self.conn.cursor()
        cursor.execute(self.__class__.GET_HASH, (username, ))
        passwdhash = cursor.fetchone()
        if not passwdhash:
            return False
        hashed_pass = passwdhash['password']
        if PasswdCheckHash.verify_password(password, hashed_pass):
            cursor.execute(self.__class__.GET_LOGIN, (username, hashed_pass))
            usr_credentials = cursor.fetchone()

            return Client(usr_credentials['id'], usr_credentials['username'],
                          usr_credentials['balance'], usr_credentials['message'])

        return False

    def change_pass(self, new_pass, logged_user):
        hashpassw = PasswdCheckHash.hash_password(new_pass)
        cursor = self.conn.cursor()
        cursor.execute(self.__class__.CHANGE_PASS, (hashpassw, logged_user.get_id()))
        self.conn.commit()

        if self.login(logged_user.get_username(), new_pass):
            return True

        return False
