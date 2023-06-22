import sqlite3
import os
from tkinter import messagebox

def connect():
    ''' Create a database if not existed and make a connection to it.
    
    '''
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS students (num Integer PRIMARY KEY, name TEXT, id TEXT, sex TEXT, year TEXT, code TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS courses (num Integer PRIMARY KEY,code TEXT, course TEXT)")
    conn.commit()
    conn.close()

def insert_students(name,id,sex,year,code):
    ''' insertion function to insert a new student to the database.
    
        A.
    '''
    if not all((name,id,sex,year,code)):
        messagebox.showerror("Error", "Student Fields must be filled.")
        return
    
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM courses WHERE code = ?", (code,))
    result = cur.fetchone()
    if result is None:
        messagebox.showerror("Error", f"Course '{code}' does not exist")
        conn.close()

    cur.execute("SELECT * FROM students WHERE id = ?", (id,))
    result = cur.fetchone()
    if result is not None:
        messagebox.showerror("Error", f"Student '{id}' already exists.")
        conn.close()

    cur.execute("INSERT INTO students Values (NULL,?,?,?,?,?)",(name,id,sex,year,code))
    conn.commit()
    conn.close()

def insert_courses(code,course):
    if not all((code,course)):
        messagebox.showerror("Error", "Course fields must be filled.")
        return
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO courses Values (NULL,?,?)",(code,course,))
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

def search(name="",id="",sex="",year="",code=""):
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("Select * FROM students WHERE name=? or id=? or sex=? or year=? or code=?",(name,id,sex,year,code))
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

def update_students(num,name,id,sex,year,code):
    if not all((num,name,id,sex,year,code)):
        messagebox.showerror("Error", "Student fields must be filled.")
        return
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("UPDATE students SET name=?, id=?, sex=?, year=?,code=? WHERE num=?",(name,id,sex,year,code,num))
    conn.commit()
    conn.close()

def update_courses(num,name,course):
    if not all((num,num,name,course)):
        messagebox.showerror("Error", "Course fields must be filled.")
        return
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("UPDATE courses SET code=?, course=? WHERE num=?",(name,course,num))
    conn.commit()
    conn.close()

def delete_data():
    
    if os.path.exists("Students.db"):
        os.remove("Students.db")
    connect()
connect()
