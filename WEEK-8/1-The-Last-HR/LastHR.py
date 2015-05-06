import requests
import sqlite3


class TheLastHR:

    HACKBGAPI = 'https://hackbulgaria.com/api/students/'
    HRDATABASE = 'DBs/hr-data.db'
    FOREINGKEYS = '''PRAGMA foreign_keys=ON'''

    def __init__(self):
        self.api_data = requests.get(TheLastHR.HACKBGAPI)
        self.db = sqlite3.connect(TheLastHR.HRDATABASE)
        self.cursor = self.db.cursor()

        self.cursor.execute(TheLastHR.FOREINGKEYS)

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS
            Students(
                student_id INTEGER PRIMARY KEY,
                student_name TEXT UNIQUE,
                student_github TEXT
                )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS
            Courses(
                course_id INTEGER PRIMARY KEY,
                course_name TEXT UNIQUE
                )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS
            Studen_to_Course(
                student_id INTEGER,
                course_id INTEGER,
                FOREIGN KEY(student_id) REFERENCES Students(student_id),
                FOREIGN KEY(course_id) REFERENCES Courses(course_id)
                )
        ''')

        self.db.commit()
        self.db.close()

    def populate_tables(self):
        self.db = sqlite3.connect(TheLastHR.HRDATABASE)
        self.cursor = self.db.cursor()
        self.cursor.execute(TheLastHR.FOREINGKEYS)
# Populating Students - START
        for user in self.api_data.json():

            try:
                self.cursor.execute('''
                    INSERT INTO Students(student_name)
                    VALUES(?)
                    ''', (user['name'], )
                    )
            except Exception as error:
                print (error)

            if user['github']:
                self.cursor.execute('''UPDATE Students SET student_github = ?
                    WHERE student_name is ?''', (user['github'], user['name']))

            self.cursor.execute('''SELECT student_id FROM Students
                WHERE student_name is ?''', (user['name'], ))
            studentid = self.cursor.fetchone()[0]
# Populating Students - END
# Populating Courses - START
            for course in user['courses']:
                try:
                    self.cursor.execute('''
                        INSERT INTO Courses(course_name)
                        VALUES(?)
                        ''', (course['name'], )
                        )
                except Exception as error:
                    print (error)
                self.cursor.execute('''SELECT course_id FROM Courses
                    WHERE course_name is ?''', (course['name'], ))
                courseid = self.cursor.fetchone()[0]
# Populating Courses - END
# Populating junction table - START
                self.cursor.execute('''SELECT * FROM Studen_to_Course
                    WHERE student_id= ? AND course_id= ?''', (studentid, courseid))
                student_course = self.cursor.fetchone()
                if not student_course:
                    self.cursor.execute('''
                        INSERT INTO Studen_to_Course(student_id, course_id)
                        VALUES(?, ?)
                        ''', (studentid, courseid)
                        )
# Populating junction table - END

        self.db.commit()
        self.db.close()

    def list_students_with_githubs(self):
        self.db = sqlite3.connect(TheLastHR.HRDATABASE)
        self.cursor = self.db.cursor()

        self.cursor.execute('''SELECT * FROM Students
            WHERE student_github is not null ORDER BY student_name''')
        users_githubs = self.cursor.fetchall()

        self.db.close()
        return users_githubs

    def list_courses(self):
        self.db = sqlite3.connect(TheLastHR.HRDATABASE)
        self.cursor = self.db.cursor()

        self.cursor.execute('''SELECT COUNT(Courses.course_name) AS course_acc, Courses.course_name FROM Courses
            INNER JOIN Studen_to_Course ON Courses.course_id = Studen_to_Course.course_id
            INNER JOIN Students ON Studen_to_Course.student_id = Students.student_id
            GROUP BY Courses.course_name ORDER BY course_acc''')

        courses_num_studs = self.cursor.fetchall()
        self.db.close()
        return courses_num_studs

    def list_students_courses(self):
        self.db = sqlite3.connect(TheLastHR.HRDATABASE)
        self.cursor = self.db.cursor()

        self.cursor.execute('''SELECT  Students.student_name, GROUP_CONCAT(Courses.course_name) FROM Students
            INNER JOIN Studen_to_Course ON Students.student_id = Studen_to_Course.student_id
            INNER JOIN Courses ON Studen_to_Course.course_id = Courses.course_id
            GROUP BY Students.student_name''')

        students_courses = self.cursor.fetchall()
        self.db.close()
        return students_courses

    def top_10_coursants(self):
        self.db = sqlite3.connect(TheLastHR.HRDATABASE)
        self.cursor = self.db.cursor()

        self.cursor.execute('''SELECT COUNT(Students.student_name) AS stud_acc, Students.student_name FROM Students
            INNER JOIN Studen_to_Course ON Students.student_id = Studen_to_Course.student_id
            INNER JOIN Courses ON Studen_to_Course.course_id = Courses.course_id
            GROUP BY Students.student_name
            ORDER BY stud_acc DESC LIMIT 10''')

        topcoursants = self.cursor.fetchall()
        self.db.close()
        return topcoursants


def main():

    testHR = TheLastHR()

    for row in testHR.list_students_with_githubs():
        print ('{} - {}'.format(row[1], row[2]))

    for row in testHR.list_courses():
        print ('{} studets enrolled {}'.format(row[0], row[1]))

    for row in testHR.list_students_courses():
        print ('{} has been attending {}'.format(row[0], row[1]))

    for row in testHR.top_10_coursants():
        print ('{} has been attending {} HackBGcourses'.format(row[1], row[0]))


if __name__ == '__main__':
    main()
