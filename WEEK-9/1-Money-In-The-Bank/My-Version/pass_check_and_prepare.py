import re
import uuid
import hashlib


class PasswdCheckHash:

    @staticmethod
    def passwd_check(plain_passowrd, user):
        strong_pass = r'^(?=.*[A-Z])(?=.*[!@#$&*])(?=.*[0-9])(?=.*[a-z]).{8,}$'

        if re.match(strong_pass, plain_passowrd) and \
                user.lower() not in plain_passowrd.lower():
                return True

        return False

    @staticmethod
    def hash_password(password, salt=None):
        if salt is None:
            salt = uuid.uuid4().hex

        hashed_password = hashlib.sha256((password+salt).encode('utf-8')).hexdigest()

        return (hashed_password, salt)

    @staticmethod
    def verify_password(password, hashed_password, salt):
        re_hashed, salt = PasswdCheckHash.hash_password(password, salt)

        return re_hashed == hashed_password
