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

def search(name=None, id=None, sex=None, year=None, code=None):
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()

    query = "SELECT * FROM students WHERE 1=1"

    if name:
        query += f" AND name = '{name}'"

    if id:
        query += f" AND id = '{id}'"

    if sex:
        query += f" AND sex = '{sex}'"

    if year:
        query += f" AND year = '{year}'"

    if code:
        query += f" AND code = '{code}'"

    cur.execute(query)
    results = cur.fetchall()

    conn.close()

    return results


def delete_student(num):

    conn = sqlite3.connect("Students.db")
    cur  = conn.cursor()
    cur.execute("DELETE FROM students WHERE num=?",(num,))
    conn.commit()
    conn.close()
    
def delete_course(num):
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()

    # Retrieve the course details before deleting
    cur.execute("SELECT code, course FROM courses WHERE num=?", (num,))
    result = cur.fetchone()

    if result is None:
        messagebox.showerror("Error", "Course not found.")
        conn.close()
        return

    code = result[0]
    course = result[1]

    # Double confirmation
    confirmation = messagebox.askyesno("Confirmation", f"Are you sure you want to delete the course: {course}?\n"
                                                      f"All associated students with the old course will also be deleted.")


    if confirmation:
        # Delete the course
        cur.execute("DELETE FROM courses WHERE num=?", (num,))
        conn.commit()
        cur.execute("DELETE FROM students WHERE code=?", (code,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Course deleted successfully.")
    else:
        messagebox.showinfo("Deletion Canceled", "Deletion operation canceled.")


def update_students(num,name,id,sex,year,code):

    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM courses WHERE code = ?", (code,))
    result = cur.fetchone()
    if result is None:
        messagebox.showerror("Error", f"Course '{code}' does not exist")
        conn.close()

    cur.execute("SELECT * FROM students WHERE num=?", (num,))
    result = cur.fetchone()


    stored_id = result[2]  # Get the stored id from the fetched result

    if id != stored_id:
        # Check if the new id is different from the stored id
        cur.execute("SELECT * FROM students WHERE id=?", (id,))
        result = cur.fetchone()
        if result is not None:
            messagebox.showerror("Error", f"Student with ID '{id}' already exists")
            conn.close()
            return
        
    cur.execute("UPDATE students SET name=?, id=?, sex=?, year=?,code=? WHERE num=?",(name,id,sex,year,code,num))
    conn.commit()
    conn.close()

def update_courses(num, code, course):
    if not all((num, code, course)):
        messagebox.showerror("Error", "Course fields must be filled.")
        return

    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()

    # Retrieve the old course details before updating
    cur.execute("SELECT code, course FROM courses WHERE num=?", (num,))
    result = cur.fetchone()

    if result is None:
        messagebox.showerror("Error", "Course not found.")
        conn.close()
        return

    old_code = result[0]
    old_course = result[1]

    # Double confirmation
    confirmation = messagebox.askyesno("Confirmation", f"Are you sure you want to update the course: {old_code} - {old_course}?\n"
                                                      f"All associated students with the old course will also be updated.")

    if confirmation:
        # Update the course details
        cur.execute("UPDATE courses SET code=?, course=? WHERE num=?", (code, course, num))
        conn.commit()

        # Update the course code for associated students
        cur.execute("UPDATE students SET code=? WHERE code=?", (code, old_code))

        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Course and associated students updated successfully.")
    else:
        messagebox.showinfo("Update Canceled", "Update operation canceled.")


    conn.commit()
    conn.close()


def delete_data():
    
    if os.path.exists("Students.db"):
        os.remove("Students.db")
    connect()
connect()
