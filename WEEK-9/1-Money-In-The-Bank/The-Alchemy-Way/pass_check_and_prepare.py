import re
from passlib.hash import pbkdf2_sha256


class PasswdCheckHash:

    @staticmethod
    def passwd_check(plain_passowrd, user):
        strong_pass = r'^(?=.*[A-Z])(?=.*[!@#$&*])(?=.*[0-9])(?=.*[a-z]).{8,}$'

        if re.match(strong_pass, plain_passowrd) and \
                user.lower() not in plain_passowrd.lower() and\
                len(user) >= 6:
                return True

        print (PasswdCheckHash.__strong_psswd_inf())
        return False

    @staticmethod
    def hash_password(password):
        hashpasswd = pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=32)

        return hashpasswd

    @staticmethod
    def verify_password(password, hashpasswd):
        return pbkdf2_sha256.verify(password, hashpasswd)

    @staticmethod
    def __strong_psswd_inf():
        strong_psswd_msg = ["Failed! Your Passwd/Username Should:",
                            "",
                            "Have More then 8 symbols",
                            "Must have capital letters, and numbers and a special symbol",
                            "Username is not in the password (as a substring)",
                            "Username shoud be longer than 6 symbols"]
        return "\n".join(strong_psswd_msg)
