#!/usr/bin/python3
import unittest
import datetime
from bank_account import BankAccount


class BankAccountTest(unittest.TestCase):

    def setUp(self):
        self.test_acc = BankAccount("Testy", 10, "BGN")
        self.virtual_acc = BankAccount("VirtualACC", 0, "BGN")

    def test_init(self):
        with self.assertRaises(TypeError):
            self.bad_acc = BankAccount(5, "Bad Bad", 32)
        with self.assertRaises(ValueError):
            self.bad_acc = BankAccount("Testy", -100, "BGN")

    def test_str(self):
        self.assertEqual(str(self.test_acc), "Bank account for Testy with balance of 10BGN")

    def test_int(self):
        self.assertEqual(self.test_acc.balance, int(self.test_acc))

    def test_create_new_account(self):
        self.assertTrue(isinstance(self.test_acc, BankAccount))

    def test_valid_deposit_amount(self):
        with self.assertRaises(ValueError):
            self.test_acc.deposit_amount(-110)
        self.new_deposit = self.test_acc.deposit_amount(10)
        self.assertGreaterEqual(self.test_acc.balance, self.new_deposit)

    def test_check_balance(self):
        self.assertEqual(self.test_acc.check_balance(), 10)

    def test_withdraw(self):
        self.assertTrue(self.test_acc.withdraw(5))

    def test_transffering(self):
        with self.assertRaises(ValueError):
            self.test_acc.transffering_to(self.virtual_acc, 1000)
        self.test_acc.transffering_to(self.virtual_acc, 5)
        self.assertEqual(int(self.virtual_acc), 5)

    def test_acc_history(self):
        test_history = []
        test_history.append("{}: Acount was Created".format(datetime.datetime.now().strftime("%Y/%m/%d %H:%M")))
        self.assertListEqual(self.test_acc.history, test_history)


if __name__ == '__main__':
    unittest.main()
