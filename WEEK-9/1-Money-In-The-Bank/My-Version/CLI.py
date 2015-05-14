import readline
import getpass


class BankInterface:

    GREET_MSG = "Welcome to our bank service. You are not logged in. \nPlease type 'help' if you need it"

    def __init__(self):
        pass

    def create_help(self):
        cli_help = ["Here is the list of commands:",
                    "",
                    "login              : Logs you in the system",
                    "register           : Make registration (new users)",
                    "exit               : Exitting from system @ any time"]
        return "\n".join(cli_help)

    def parse_command(self, command):
        return tuple(command.split(" "))

    def is_command(self, command_tuple, command_string):
        return command_tuple[0] == command_string

    def trigger_unknown_command(self):
        unknown_command = ["Error: Unknown command!",
                           "Why don't you type help,",
                           "to see a list of commands."]

        return "\n".join(unknown_command)

    def take_user_data(self, step, data_type):

        while True:
            try:
                if 'pass' in step:
                    data = getpass.getpass(prompt=step)
                    return data
                data = input(step)
                if self.is_give_up(data):
                    return False
                if not data:
                    continue
                else:
                    return data_type(data)
            except Exception as e:
                print(e)

    def is_give_up(self, data):
        return data == 'exit'

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
        return usr_pass

    def main_menu(self, manager):
        print (self.GREET_MSG)

        while True:

            command = self.parse_command(input("Enter command$ "))

            if self.is_command(command, 'help'):
                print(self.create_help())

            elif self.is_command(command, 'register'):
                usr_pass = self.start_register()
                if usr_pass:
                    if manager.register(usr_pass[0], usr_pass[1]):
                        print ('{} Registered Successfuly'.format(usr_pass[0]))
                        continue
                    print ('Registration Failed')

            elif self.is_command(command, 'login'):
                print ('Welcome to Login Procedure')
                user = self.parse_command(input("Enter User: "))
                passwd = getpass.getpass("Enter Pass: ")

                logged_user = manager.login(user[0], passwd)
                if logged_user:
                    print("Successfuly Logged")
                else:
                    print("Login failed")

            elif self.is_give_up(command[0]):
                print ('Bye Bye')
                break

            else:
                if command[0] is '':
                    continue
                print (self.trigger_unknown_command())
