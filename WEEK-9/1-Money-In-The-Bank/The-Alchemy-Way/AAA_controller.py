import datetime
from models import Client, LoginAttempt

from pass_check_and_prepare import PasswdCheckHash


class AuthenticationController:

    def __init__(self, session, block_after_n_logins=5, block_for_n_minutes=5):
        self.__session = session
        self.__settings = {
            'block_after_n_logins': block_after_n_logins,
            'block_for_n_minutes': block_for_n_minutes
        }

    def __commit_changes(self, objects):
        self.__session.add_all(objects)
        self.__session.commit()

    def __is_registered(self, username):
        try:
            user = self.__session.query(Client).filter(Client.username == username).one()
            return user
        except:
            return None

    def __unblock_user(self, user):
        user.is_blocked = False
        user.blocked_until = None

        # Break last 5 failed attempts
        user.login_attempts.append(LoginAttempt(attempt_status=LoginAttempt.AFTER_BLOCK, user_id=user.id))
        self.__commit_changes([user])

    def __block_user(self, user):
        user.is_blocked = True
        delta_time = datetime.timedelta(minutes=self.__settings['block_for_n_minutes'])
        user.blocked_until = (datetime.datetime.utcnow()+delta_time)
        self.__commit_changes([user])

    def __can_log_after_block(self, user):
        now = datetime.datetime.utcnow()
        return now >= user.blocked_until

    def __can_login(self, user):
        if user.is_blocked:
            if self.__can_log_after_block(user):
                self.__unblock_user(user)
                return True
            return False

        block_after_n_logins = self.__settings['block_after_n_logins']

        login_attempts = self.__session.query(LoginAttempt).\
            filter(LoginAttempt.user_id == user.id).\
            order_by(LoginAttempt.attempt_timestamp.desc()).\
            limit(block_after_n_logins)

        last_n_failed = [att.attempt_status == LoginAttempt.FAILED_ATTEMPT for att in login_attempts]

        if len(last_n_failed) < block_after_n_logins:
            return True

        if all(last_n_failed):
            self.__block_user(user)
            return False

        return True

    def __success_login_attempt(self, user):
        user.login_attempts.append(LoginAttempt(attempt_status=LoginAttempt.SUCCESSFUL_ATTEMPT, user_id=user.id))
        self.__commit_changes([user])

    def __failed_login_attempt(self, user):
        user.login_attempts.append(LoginAttempt(attempt_status=LoginAttempt.FAILED_ATTEMPT, user_id=user.id))
        self.__commit_changes([user])

    def register(self, username, password):
        if self.__is_registered(username) is not None:
            return False

        if not PasswdCheckHash.passwd_check(password, username):
            return False

        client = Client(username=username,
                        password=PasswdCheckHash.hash_password(password),
                        is_blocked=False,
                        blocked_until=None)

        self.__commit_changes([client])

        return True

    def login(self, username, password):
        user = self.__is_registered(username)

        if user is None:
            return 'No such user'

        if not self.__can_login(user):
            return 'User {} is Blocked'.format(user.username)

        is_passwd = PasswdCheckHash.verify_password(password, user.password)

        if is_passwd:
            self.__success_login_attempt(user)
            return user

        self.__failed_login_attempt(user)
        return 'Failed Login'

    def change_password(self, client, password):
        if PasswdCheckHash.passwd_check(password, client.username):
            client.password = PasswdCheckHash.hash_password(password)
            self.__commit_changes([client])

            if self.login(client.username, password):
                return True

        return False
