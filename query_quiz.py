import sqlite3 


connection = sqlite3.connect('hw13.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO student (first_name, last_name) VALUES ('James', 'Smith')")
cur.execute("INSERT INTO student (first_name, last_name) VALUES ('Diana', 'Greene')")
cur.execute("INSERT INTO student (first_name, last_name) VALUES ('Sara', 'White')")
cur.execute("INSERT INTO student (first_name, last_name) VALUES ('Williams', 'Gibson')")
cur.execute("INSERT INTO student (first_name, last_name) VALUES ('Doreen', 'Paul')")
cur.execute("INSERT INTO student (first_name, last_name) VALUES ('Wilbert', 'Andre')")

cur.execute("INSERT INTO quiz (subject, questions, quiz_date) VALUES ('Math', 20, 'February 20, 2022')")
cur.execute("INSERT INTO quiz (subject, questions, quiz_date) VALUES ('English', 40, 'January 12, 2021')")
cur.execute("INSERT INTO quiz (subject, questions, quiz_date) VALUES ('Spanish', 15, 'March 12, 2019')")
cur.execute("INSERT INTO quiz (subject, questions, quiz_date) VALUES ('Computer Science 101', 30, 'August 12, 2022')")
cur.execute("INSERT INTO quiz (subject, questions, quiz_date) VALUES ('Calculus 112', 40, 'October 1, 2019')")
cur.execute("INSERT INTO quiz (subject, questions, quiz_date) VALUES ('Biology 102', 30, 'November 12, 2021')")


cur.execute("INSERT INTO student_result (student_id, quiz_id, grade) VALUES (2, 2, 60)")
cur.execute("INSERT INTO student_result (student_id, quiz_id, grade) VALUES (3, 4, 90)")
cur.execute("INSERT INTO student_result (student_id, quiz_id, grade) VALUES (5, 3, 50)")
cur.execute("INSERT INTO student_result (student_id, quiz_id, grade) VALUES (4, 4, 95)")
cur.execute("INSERT INTO student_result (student_id, quiz_id, grade) VALUES (2, 3, 65)")
cur.execute("INSERT INTO student_result (student_id, quiz_id, grade) VALUES (1, 1, 75)")

connection.commit()
connection.close()
