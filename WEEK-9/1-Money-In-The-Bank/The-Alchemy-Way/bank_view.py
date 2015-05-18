import readline
import getpass


class BankView:

    GREET_MSG = "Welcome to our bank service. You are not logged in. \nPlease type 'help' if you need it"

    def __init__(self, bank_controller):
        self.__controller = bank_controller

    def create_help(self):
        cli_help = ["Here is the list of commands:",
                    "",
                    "login              : Logs you in the system",
                    "register           : Make registration (new users)",
                    "exit               : Exitting from system @ any time"]
        return "\n".join(cli_help)

    def logged_help(self):
        logg_help = ["Here is the list of commands in logged mode:",
                     "",
                     "info              : for showing account info",
                     "changepass        : for changing passowrd",
                     "logout            : Returns you in the Main Menu"]
        return "\n".join(logg_help)

    def create_info(self, logged_user):
        cli_info = ["Your username is: {}".format(logged_user.username),
                    "Your id is: {}".format(logged_user.id)]
        return "\n".join(cli_info)

    def strong_psswd_inf(self):
        strong_psswd_msg = ["Your Passwd Should:",
                            "",
                            "Have More then 8 symbols",
                            "Must have capital letters, and numbers and a special symbol",
                            "Username is not in the password (as a substring)"]
        return "\n".join(strong_psswd_msg)

    def trigger_unknown_command(self):
        unknown_command = ["Error: Unknown command!",
                           "Why don't you type help,",
                           "to see a list of commands."]

        return "\n".join(unknown_command)

    def parse_command(self, command):
        return tuple(command.split(" "))

    def is_command(self, command_tuple, command_string):
        return command_tuple[0] == command_string

    def is_give_up(self, command):
        return command == 'exit' or command == 'logout'

    def take_user_data(self, step, data_type, user=None):

        while True:
            try:

                if 'pass' in step.lower():
                    passwd = getpass.getpass(prompt=step)
                    if self.is_give_up(passwd):
                        return False
                    return passwd

                data = input(step)
                if self.is_give_up(data):
                    return False
                if not data:
                    continue
                else:
                    return data_type(data)

            except Exception as e:
                print(e)

    def start_register(self):
        register_steps = [("Step 1(usr_name):", str),
                          ("Step 2(password):", str)]
        usr_pass = []

        print ('Welcome to the Register Form! Just follow the steps!')
        while register_steps:
            current_step, data_type = register_steps[0]
            register_steps.pop(0)
            data = self.take_user_data(current_step, data_type)

            if not data:
                print ('Registration Abborted')
                return False
            usr_pass.append(data)

        if self.__controller.register(usr_pass[0], usr_pass[1]):
            print ('{} Registered Successfuly'.format(usr_pass[0]))
            return True
        print ('Registration Failed')
        return False

    def start_auth(self):
        print ('Welcome to Login Procedure')
        user = self.take_user_data("Enter User: ", str)
        passwd = getpass.getpass('Enter passwd: ')

        logged_user = self.__controller.login(user, passwd)
        if not isinstance(logged_user, str):
            return logged_user

        print (logged_user)
        return False

    def main_menu(self):
        print (self.GREET_MSG)

        while True:

            command = self.parse_command(input("Enter command$ "))

            if self.is_command(command, 'help'):
                print(self.create_help())

            elif self.is_command(command, 'register'):
                self.start_register()

            elif self.is_command(command, 'login'):
                logged_user = self.start_auth()
                if logged_user:
                    self.logged_menu(logged_user)

            elif self.is_give_up(command[0]):
                print ('Bye Bye')
                break

            else:
                if command[0] is '':
                    continue
                print (self.trigger_unknown_command())

    def logged_menu(self, logged_user):
        print("Welcome you are logged in as: " + logged_user.username)

        while True:
            command = self.parse_command(input("Enter command# "))

            if self.is_command(command, 'info'):
                print(self.create_info(logged_user))

            elif self.is_command(command, 'help'):
                print(self.logged_help())

            elif self.is_command(command, 'changepass'):
                msg = 'Your New Password: '
                new_pass = self.take_user_data(msg, str, logged_user.get_username())
                if self.__controller.change_pass(new_pass, logged_user):
                    print ('Your Password is changed successfuly')
                else:
                    print ('Something went wrong ?!')

            elif self.is_give_up(command[0]):
                print ('Returning to the MAIN MENU!')
                break

            else:
                if command[0] is '':
                    continue
                print (self.trigger_unknown_command())
