class Client():
    def __init__(self, usr_id, username, balance, message):
        self.__username = username
        self.__balance = balance
        self.__usr_id = usr_id
        self.__message = message

    def __repr__(self):
        return 'User: {}, ID: {}, Balance: {}'\
                .format(self.__username,  self.__usr_id, self.__balance)

    def get_username(self):
        return self.__username

    def get_balance(self):
        return self.__balance

    def get_id(self):
        return self.__usr_id

    def get_message(self):
        return self.__message

    def set_message(self, new_message):
        self.__message = new_message
