DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS quiz;
DROP TABLE IF EXISTS student_result;




CREATE TABLE student (
    id integer primary key AUTOINCREMENT,
    first_name text not null,
    last_name text not null
);


CREATE TABLE quiz (
    id integer primary key AUTOINCREMENT,
    subject text not null,
    questions integer,
    quiz_date TEXT Not null

);


CREATE TABLE student_result (
    student_id integer,
    quiz_id integer,
    grade
);

