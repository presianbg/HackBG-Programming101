import sys
import unittest
sys.path.append("..")
from pass_check_and_prepare import PasswdCheckHash


class TestPasswordChecker(unittest.TestCase):

    def test_weak_passwd(self):
        self.assertFalse(PasswdCheckHash.passwd_check('weakpass', 'user1'))

    def test_user_in_passwd(self):
        self.assertFalse(PasswdCheckHash.passwd_check('Ver1Str0Ng9Pa$$', 'Ver1'))

    def test_strong_passwd(self):
        self.assertTrue(PasswdCheckHash.passwd_check('Ver1Str0Ng9Pa$$', 'MegaUsr'))

    def test_without_num(self):
        self.assertFalse(PasswdCheckHash.passwd_check('VersStrNgsPa$$', 'MegaUsr'))

    def test_without_upper(self):
        self.assertFalse(PasswdCheckHash.passwd_check('ver1str0ng9pa$$', 'MegaUsr'))

    def test_without_lower(self):
        self.assertFalse(PasswdCheckHash.passwd_check('VER1STR0NG9PA$$', 'MegaUsr'))

    def test_without_spec(self):
        self.assertFalse(PasswdCheckHash.passwd_check('Ver1Str0Ng9PaSs', 'MegaUsr'))

    def test_under_8(self):
        self.assertFalse(PasswdCheckHash.passwd_check('VStr0Ng', 'MegaUsr'))

    def test_salted_hash(self):
        hpass, salt = PasswdCheckHash.hash_password('Ver1Str0Ng9Pa$$')
        self.assertTrue(PasswdCheckHash.verify_password('Ver1Str0Ng9Pa$$', hpass, salt))
        self.assertFalse(PasswdCheckHash.verify_password('VerGGtr0Ng9Pa$$', hpass, salt))
        salt = '1efb159c089c42108a237526f7b23c92'
        self.assertFalse(PasswdCheckHash.verify_password('Ver1Str0Ng9Pa$$', hpass, salt))

if __name__ == '__main__':
    unittest.main()
