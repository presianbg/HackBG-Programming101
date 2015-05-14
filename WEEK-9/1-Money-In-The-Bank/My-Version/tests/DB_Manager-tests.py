import sys
import unittest
import os
sys.path.append("..")
from test_settings import DB_NAME, SQL_STRUCT_FILE
from database_manager import DataBankManager


class DbManagerTests(unittest.TestCase):

    def setUp(self):
        self.manager = DataBankManager.create_db_sql(SQL_STRUCT_FILE, DB_NAME,
                                                     create_if_exists=True)
        self.assertTrue(self.manager.register('WadaFaka', 'PlainPasswordHere'))

    @classmethod
    def tearDownClass(cls):
        os.remove(DB_NAME)

    def test_creating_db_file(self):
        self.assertTrue(os.path.exists(DB_NAME))

    def test_reg_already_reg_user(self):
        self.assertFalse(self.manager.register('WadaFaka', 'PlainPasswordHere'))

    def test_register_new(self):
        self.assertTrue(self.manager.register('FooFoo', 'YourPassIsWEAK'))

    def test_login_as_unknowuser(self):
        self.assertFalse(self.manager.login('Alabala', 'Waafaka?'))

    def test_login_as_knownuser(self):
        self.assertTrue(self.manager.login('WadaFaka', 'PlainPasswordHere'))
        print (self.manager.login('WadaFaka', 'PlainPasswordHere'))

    def test_with_wrong_pass(self):
        self.assertFalse(self.manager.login("' OR 1 = 1 --", 'PlainPas!?swordHere'))

    def test_change_pass_no_logged(self):
        with self.assertRaises(AttributeError):
            self.manager.change_pass('Alabala', 1)

    def test_change_pass(self):
        logged_usr = self.manager.login('WadaFaka', 'PlainPasswordHere')
        new_pass = 'GuemiRuki'
        self.assertTrue(self.manager.change_pass(new_pass, logged_usr))

        log_with_npass = self.manager.login('WadaFaka', new_pass)
        self.assertEqual(log_with_npass.get_username(), 'WadaFaka')

if __name__ == '__main__':
    unittest.main()
