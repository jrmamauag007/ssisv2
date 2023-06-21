import sqlite3
import os
from tkinter import messagebox

def connect():
    ''' Create a database if not existed and make a connection to it.
    
    '''
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS students (num Integer PRIMARY KEY, fn TEXT, ln TEXT, id TEXT, course TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS courses (num Integer PRIMARY KEY, name TEXT)")
    conn.commit()
    conn.close()

def insert_students(fn,ln,id,course):
    ''' insertion function to insert a new student to the database.
    
        A.
    '''
    if not all((fn, ln, id, course)):
        messagebox.showerror("Error", "All fields must be filled.")
        return
    
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM courses WHERE name = ?", (course,))
    result = cur.fetchone()
    if result is None:
        messagebox.showerror("Error", f"Course '{course}' does not exist")
        conn.close()

    cur.execute("SELECT * FROM students WHERE id = ?", (id,))
    result = cur.fetchone()
    if result is not None:
        messagebox.showerror("Error", f"Student '{id}' already exists.")
        conn.close()

    cur.execute("INSERT INTO students Values (NULL,?,?,?,?)",(fn,ln,id,course))
    conn.commit()
    conn.close()

def insert_courses(name):
    ''' insertion function to insert a new student to the database.
    
        A.
    '''
    if not all((name)):
        messagebox.showerror("Error", "Course field must be filled.")
        return
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO courses Values (NULL,?)",(name))
    conn.commit()
    conn.close()

def view_students():
    
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    conn.close()
    return rows

def view_courses():
   
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM courses")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(fn="",ln="",id="",course=""):
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("Select * FROM students WHERE fn=? or ln=? or id=? or course=?",(fn,ln,id,course))
    rows = cur.fetchall()
    conn.close()
    return(rows)

def delete_student(num):

    conn = sqlite3.connect("Students.db")
    cur  = conn.cursor()
    cur.execute("DELETE FROM students WHERE num=?",(num,))
    conn.commit()
    conn.close()
def delete_course(num):

    conn = sqlite3.connect("Students.db")
    cur  = conn.cursor()
    cur.execute("DELETE FROM courses WHERE num=?",(num,))
    conn.commit()
    conn.close()

def update_students(num,fn,ln,id,course):

    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("UPDATE students SET fn=?, ln=?, id=?, course=? WHERE num=?",(fn,ln,id,course,num))
    conn.commit()
    conn.close()

def update_courses(num,name):

    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("UPDATE courses SET name=? WHERE num=?",(name,num))
    conn.commit()
    conn.close()

def delete_data():
    
    if os.path.exists("Students.db"):
        os.remove("Students.db")
    connect()
connect()