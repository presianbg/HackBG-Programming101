from create_litesqlDB import ManageSQL
import unittest


class TestCreateDb(unittest.TestCase):

    def test_creatingdb(self):
        db = ManageSQL()
        db.populate_data()


if __name__ == '__main__':
    unittest.main()
