

class BankInterface:

    GREET_MSG = "Welcome to our bank service. You are not logged in. \nPlease type 'help' if you need it"

    def __init__(self):
        pass

    def create_help(self):
        cli_help = ["Here is the list of commands:",
                    "",
                    "login              : Logs you in the system",
                    "register           : Make registration (new users)",
                    "exit               : Exitting from system"]
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

    @classmethod
    def main_menu(cls, manager):
        print (cls.GREET_MSG)

        while True:

            command = cls.parse_command(cls, input("Enter command$ "))

            if cls.is_command(cls, command, 'help'):
                print(cls.create_help(cls))

            elif cls.is_command(cls, command, 'register'):
                print ('Register Procedure')

            elif cls.is_command(cls, command, 'login'):
                print ('Login Procedure')

            elif cls.is_give_up(cls, command[0]):
                print ('Bye Bye')
                break

            else:
                if command[0] is '':
                    continue
                print (cls.trigger_unknown_command(cls))
