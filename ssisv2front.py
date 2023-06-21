import tkinter as tk
from tkinter import ttk
from tkinter import *
import ssisv2back
from tkinter import messagebox

def get_selected_row(event):
    ''' get_selected_row function to get content of the selected row.
    
        Arguments
        ---------
        event: a virtual interrupt.
    '''
    global selected_tuple
    if lb1.curselection() != ():
 
        index = lb1.curselection()[0]
        selected_tuple = lb1.get(index)
        clear_entries()
        e1.insert(END, selected_tuple[1])
        e2.insert(END, selected_tuple[2])
        e3.insert(END, selected_tuple[3])
        e4.insert(END, selected_tuple[4])


def viewstudents_command():
    ''' view_command function to show the output database.
    
    '''
    lb1.delete(0, END)  
    for row in ssisv2back.view_students():
        lb1.insert(END, row)

def viewcourses_command():
    ''' view_command function to show the output database.
    
    '''
    lb1.delete(0, END)  
    for row in ssisv2back.view_courses():
        lb1.insert(END, row)


def search_command():
    ''' search_command function to search in the database.
    
    '''
    lb1.delete(0, END)
    for row in ssisv2back.search(fn.get(), ln.get(), id.get(), course.get()):
        lb1.insert(END, row)
    clear_entries()


def addstudent_command():
    ''' add_command function to add a new student to the database.
    
    '''
    ssisv2back.insert_students(fn.get(), ln.get(), id.get(), course.get())
    clear_entries()
    viewstudents_command()

def addcourse_command():
    ''' add_command function to add a new student to the database.
    
    '''
    ssisv2back.insert_courses((course.get(),))
    clear_entries()
    viewcourses_command()

def updatestudent_command():
    ''' updatestudent_command function to update the data of a specific student.

    '''
    if not lb1.curselection():
        messagebox.showwarning("Warning", "No student selected.")
        return

    # Prompt for user confirmation
    confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to update the student's data?")

    if confirmation:
        ssisv2back.update_students(selected_tuple[0], fn.get(), ln.get(), id.get(), course.get())
        clear_entries()
        viewstudents_command()
    else:
        messagebox.showinfo("Update Canceled", "Update operation canceled.")


def updatecourse_command():
    ''' updatecourse_command function to update the data of a specific course.
    
    '''
    if not lb1.curselection():
        messagebox.showwarning("Warning", "No course selected.")
        return

    # Prompt for user confirmation
    confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to update the course's data?")

    if confirmation:
        ssisv2back.update_courses(selected_tuple[0], course.get())
        clear_entries()
        viewcourses_command()
    else:
        messagebox.showinfo("Update Canceled", "Update operation canceled.")

    

def deletestudent_command():
    ''' deletestudent_command function to delete the data of a specific student.
    
    '''
    if not lb1.curselection():
        messagebox.showwarning("Warning", "No student selected.")
        return

    # Prompt for user confirmation
    confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete the student's data?")

    if confirmation:
        index = lb1.curselection()[0]
        selected_tuple = lb1.get(index)
        ssisv2back.delete_student(selected_tuple[0])
        clear_entries()
        viewstudents_command()
    else:
        messagebox.showinfo("Deletion Canceled", "Deletion operation canceled.")


def deletecourse_command():
    ''' deletecourse_command function to delete the data of a specific course.
    
    '''
    if not lb1.curselection():
        messagebox.showwarning("Warning", "No course selected.")
        return

    # Prompt for user confirmation
    confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete the course's data?")

    if confirmation:
        index = lb1.curselection()[0]
        selected_tuple = lb1.get(index)
        ssisv2back.delete_course(selected_tuple[0])
        clear_entries()
        viewcourses_command()
    else:
        messagebox



def delete_data_command():
    ''' delete_data_command function to delete the database.
    
    '''
    confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete all data?")

    if confirmation:
        ssisv2back.delete_data()
        clear_entries()
        viewstudents_command()
    else:
        messagebox


def clear_entries():
    ''' clear_entries function to clear content of entries.
    
    '''
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)


def clear_command():
    ''' view_command function to clear content of Listbox.
    
    '''
    lb1.delete(0, END)
    clear_entries()

# Create the main window
window = Tk()
window.title("Student Information System")

fn = StringVar()
ln = StringVar()
id = StringVar()
course = StringVar()

# Create entry fields
e1= ttk.Entry(window,textvariable=fn)
e2 = ttk.Entry(window,textvariable= ln)
e3 = ttk.Entry(window,textvariable=id)
e4 = ttk.Entry(window,textvariable=course)

# Create labels for entry fields
ttk.Label(window, text="First Name:").grid(row=0, column=0, padx=5, pady=5)
ttk.Label(window, text="Last Name:").grid(row=1, column=0, padx=5, pady=5)
ttk.Label(window, text="ID:").grid(row=2, column=0, padx=5, pady=5)
ttk.Label(window, text="Course:").grid(row=3, column=0, padx=5, pady=5)

# Position entry fields
e1.grid(row=0, column=1, padx=5, pady=5)
e2.grid(row=1, column=1, padx=5, pady=5)
e3.grid(row=2, column=1, padx=5, pady=5)
e4.grid(row=3, column=1, padx=5, pady=5)

# Create buttons
view_students_button = ttk.Button(window, text="View Students", command=viewstudents_command)
view_courses_button = ttk.Button(window, text="View Courses", command=viewcourses_command)
add_student_button = ttk.Button(window, text="Add Student", command=addstudent_command)
add_course_button = ttk.Button(window, text="Add Course", command=addcourse_command)
update_student_button = ttk.Button(window, text="Update Student", command=updatestudent_command)
update_course_button = ttk.Button(window, text="Update Course", command=updatecourse_command)
delete_student_button = ttk.Button(window, text="Delete Student", command=deletestudent_command)
delete_course_button = ttk.Button(window, text="Delete Course", command=deletecourse_command)
search_button = ttk.Button(window, text="Search", command=search_command)
clear_button = ttk.Button(window, text="Clear", command=clear_entries)
delete_all_button = ttk.Button(window, text="Delete All", command=delete_data_command)
exit_button = ttk.Button(window, text="Exit", command=clear_command)

# Position buttons
view_students_button.grid(row=0, column=2, padx=5, pady=5)
view_courses_button.grid(row=1, column=2, padx=5, pady=5)
add_student_button.grid(row=0, column=3, padx=5, pady=5)
add_course_button.grid(row=1, column=3, padx=5, pady=5)
update_student_button.grid(row=2, column=2, padx=5, pady=5)
update_course_button.grid(row=3, column=2, padx=5, pady=5)
delete_student_button.grid(row=2, column=3, padx=5, pady=5)
delete_course_button.grid(row=3, column=3, padx=5, pady=5)
search_button.grid(row=4, column=0, padx=5, pady=5)
clear_button.grid(row=4, column=1, padx=5, pady=5)
delete_all_button.grid(row=4, column=2, padx=5, pady=5)
exit_button.grid(row=4, column=3, padx=5, pady=5)


# Create listbox and scrollbar
lb1 = tk.Listbox(window, height=10, width=70)
lb1.grid(row=5, column=0, columnspan=4, rowspan=10, padx=5, pady=5)

sc = ttk.Scrollbar(window, command=lb1.yview)
sc.grid(row=5, column=5, rowspan=10, sticky='ns')

lb1.configure(yscrollcommand=sc.set)

# Run the main event loop
window.mainloop()


