#!/usr/bin/python3


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        self.new_numerator_a = (self.numerator * other.denominator)
        self.new_numerator_b = (other.numerator * self.denominator)
        self.new_numerator = self.new_numerator_a + self.new_numerator_b
        self.new_denominator = self.denominator * other.denominator
        self.gcd = self.fractional_norm(self.new_numerator, self.new_denominator)
        if self.new_numerator // self.gcd == self.new_denominator // self.gcd:
            return (self.new_numerator // self.gcd)
        else:
            return Fraction(self.new_numerator // self.gcd, self.new_denominator // self.gcd)

    def __sub__(self, other):
        self.new_numerator_a = (self.numerator * other.denominator)
        self.new_numerator_b = (other.numerator * self.denominator)
        self.new_numerator = self.new_numerator_a - self.new_numerator_b
        self.new_denominator = self.denominator * other.denominator
        self.gcd = self.fractional_norm(self.new_numerator, self.new_denominator)
        if self.new_numerator == 0:
            return (0)
        elif self.new_numerator // self.gcd == self.new_denominator // self.gcd:
            return (self.new_numerator // self.gcd)
        else:
            return Fraction(self.new_numerator // self.gcd, self.new_denominator // self.gcd)

    def __mul__(self, other):
        self.new_numerator = (self.numerator * other.numerator)
        self.new_denominator = (self.denominator * other.denominator)
        self.gcd = self.fractional_norm(self.new_numerator, self.new_denominator)
        if self.new_numerator // self.gcd == self.new_denominator // self.gcd:
            return (self.new_numerator // self.gcd)
        else:
            return Fraction(self.new_numerator // self.gcd, self.new_denominator // self.gcd)

    def __eq__(self, other):
        if (self.numerator / self.denominator) == (other.numerator / other.denominator):
            return True
        else:
            return False

    def fractional_norm(self, new_numerator, new_denominator):
        self.gcd_num = new_numerator
        self.gcd_denom = new_denominator
        while self.gcd_denom:
            self.gcd_num, self.gcd_denom = self.gcd_denom, self.gcd_num % self.gcd_denom
        return (self.gcd_num)


a = Fraction(1, 2)
b = Fraction(2, 4)

print (a == b)
