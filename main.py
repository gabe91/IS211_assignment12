from flask import Flask, render_template, redirect, url_for, request, g, session
import sqlite3



app = Flask(__name__)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('hw13.db')
    
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()



@app.route('/')
def index():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'password':
            error = "Invalid Credentials. Please try again."
        else:
            return redirect(url_for('dashboard'))
    return render_template('login.html', error=error)





@app.route('/dashboard')
def dashboard():
    cursor = get_db().cursor()
    
    students = cursor.execute("select first_name, last_name from student").fetchall()
    quizzes = cursor.execute("select subject, questions, quiz_date from quiz").fetchall()
    return render_template('dashboard.html', students = students, quizzes=quizzes) #quizes = quizes


@app.route('/enternew')
def new_student():
    return render_template('student.html')

@app.route("/add", methods=['POST', 'GET'])
def add_student():
    if request.method == 'POST':
        try:
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            subject = request.form['subject']
            questions = request.form['questions']
            quiz_date = request.form['quiz_date']


            with sqlite3.connect('hw13.db') as con:

                cur = con.cursor()
                cur.execute("INSERT INTO student (first_name, last_name) VALUES (?,?)",(first_name, last_name) )
                cur.execute("INSERT INTO quiz (subject, questions, quiz_date) VALUES (?,?,?)",(subject, questions, quiz_date) )
                con.commit()
                msg = "You have added the student. Thank you"
        except:
            con.rollback()
            msg = "Error! Please add student"
        finally:
            return render_template("result.html", msg=msg)
    con.close()

@app.route('/showstudents')
def showstudents():
    conn = get_db().cursor()
    students = conn.execute("select student_id, grade from student_result")

    return render_template('showstudents.html', students=students)


@app.route("/searchstudent", methods=['POST', 'GET'])
def search_student():
    if request.method == 'POST':
        student_id = request.form['student_id']
        conn = get_db().cursor()
        students = conn.execute("select student_id, grade from student_result where student_id = ?", (student_id))
        return render_template('showstudent.html', students=students)
    return render_template("searchstudent.html")

if __name__ == '__main__':
    app.run()





