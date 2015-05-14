from CLI import BankInterface
from database_manager import DataBankManager
from settings import DB_NAME, SQL_STRUCT_FILE


def main():
    manager = DataBankManager.create_db_sql(SQL_STRUCT_FILE, DB_NAME)
    BankInterface.main_menu(manager)
    manager.conn.close()

if __name__ == '__main__':
    main()
