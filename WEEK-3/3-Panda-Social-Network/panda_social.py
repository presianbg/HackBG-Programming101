#!/usr/bin/python3
import re


class Panda:
    def __init__(self, name, email, gender):
        pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if type(name) != str or type(email) != str or type(gender) != str:
            raise TypeError
        if not re.match(pattern, email):
            raise InvalidMail
        if not (gender == "female" or gender == "male"):
            raise InvalidGender
        self.name = name
        self.email = email
        self.gender = gender

    def __str__(self):
        return "Hello, I'm {}, contact me at {}, don't worry i'm {} panda".format(self.name, self.email, self.gender)

    def __repr__(self):
        return "Panda('{}', '{}', '{}')".format(self.name, self.email, self.gender)

    def __hash__(self):
        return hash(self.name + self.gender)

    def __eq__(self, other):
        equal_name = self.name == other.name
        equal_email = self.email == other.email
        equal_gender = self.gender == other.gender
        if equal_name and equal_email and equal_gender:
            return True
        return False

    def get_name(self):
        return self.name

    def get_mail(self):
        return self.email

    def get_gender(self):
        return self.gender

    def isFemale(self):
        return self.gender == "female"

    def isMale(self):
        return self.gender == "male"


class InvalidMail(Exception):
    pass


class InvalidGender(Exception):
    pass


def main():

    poonchoo = Panda("PoonChoo", "pancho@pandaland.cn", "male")
    print(poonchoo.__hash__())


if __name__ == '__main__':
    main()
