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
    ssisv2back.delete_data()
    viewstudents_command()


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


wind = Tk()

fn = StringVar()
ln = StringVar()
id = StringVar()
course = StringVar()

l0 = Label(wind, text="Student", width="10", fg="blue")
l0.config(font=("Courier", 14))

l00 = Label(wind, text="Information", width="10", fg="blue")
l00.config(font=("Courier", 14))

l000 = Label(wind, text="System", width="10", fg="blue")
l000.config(font=("Courier", 14))

l1 = Label(wind, text="First Name", width="10")
l2 = Label(wind, text="Last Name", width="10")
l3 = Label(wind, text="ID", width="10")
l4 = Label(wind, text="Course", width="10")

e1 = Entry(wind, textvariable=fn)
e2 = Entry(wind, textvariable=ln)
e3 = Entry(wind, textvariable=id)
e4 = Entry(wind, textvariable=course)

b1 = Button(wind, text="View all students", width="15", command=viewstudents_command)
b2 = Button(wind, text="View all courses", width="15", command=viewcourses_command)
b3 = Button(wind, text="Search", width="15", command=search_command)
b4 = Button(wind, text="Add New student", width="15", command=addstudent_command)
b5 = Button(wind, text="Add New course", width="15", command=addcourse_command)
b6 = Button(wind, text="Update student", width="15", command=updatestudent_command)
b7 = Button(wind, text="Update course", width="15", command=updatecourse_command)
b8 = Button(wind, text="Delete student", width="15", command=deletestudent_command)
b9 = Button(wind, text="Delete course", width="15", command=deletecourse_command)
b10 = Button(wind, text="Clear", width="15", command=clear_command)
b11 = Button(wind, text="Delete all", width="15", command=delete_data_command)
b12 = Button(wind, text="Exit", width="15", command=wind.destroy)

lb1 = Listbox(wind, height=6, width=35)
lb1.bind('<<ListboxSelect>>', get_selected_row)

sc = Scrollbar(wind)

l0.grid(row=0, column=1)
l00.grid(row=0, column=2)
l000.grid(row=0, column=3)
l1.grid(row=1, column=0)
l2.grid(row=1, column=2)
l3.grid(row=2, column=0)
l4.grid(row=2, column=2)

e1.grid(row=1, column=1)
e2.grid(row=1, column=3)
e3.grid(row=2, column=1)
e4.grid(row=2, column=3)

b1.grid(row=4, column=3)
b2.grid(row=5, column=3)
b3.grid(row=6, column=3)
b4.grid(row=7, column=3)
b5.grid(row=8, column=3)
b6.grid(row=9, column=3)
b7.grid(row=10, column=3)
b8.grid(row=11, column=3)
b9.grid(row=12, column=3)
b10.grid(row=13, column=3)
b11.grid(row=14, column=3)
b12.grid(row=14, column=4)


lb1.grid(row=4, column=0, rowspan=12, columnspan=2)

sc.grid(row=4, column=2, rowspan=12)

lb1.configure(yscrollcommand=sc.set)
sc.configure(command=lb1.yview)

wind.mainloop()
