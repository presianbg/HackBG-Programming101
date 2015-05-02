import sqlite3


class ManageSQL:

    def __init__(self):
        self.db = sqlite3.connect('DBs/employee.db')
        self.cursor = self.db.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees(id INTEGER PRIMARY KEY, name TEXT,
                monthly_salary INTEGER CHECK(monthly_salary>0), yearly_bonus INTEGER CHECK(yearly_bonus>0), position TEXT)
        ''')
        self.db.commit()

    def populate_data(self):
        names = ['Presian Ya.', 'Sashko H.', 'Nachalnika I.', 'Mitaka D.', 'Svetla A.']
        mounth_salaries = [5000, 5500, 10000, 3000, 8000]
        y_bouns = [10000, 9999, 100000, 1000, 10000]
        positions = ['Network Adm Lvl 5', 'VoIP Expert', 'DA Boss', 'Windows Master', 'Network Adm Lvl 99']

        for numb_e, employee in enumerate(names):
            self.cursor.execute('''
                INSERT INTO employees(name, monthly_salary, yearly_bonus, position)
                VALUES(?, ?, ?, ?)
                ''', (employee, mounth_salaries[numb_e], y_bouns[numb_e], positions[numb_e])
                )
        self.db.commit()
