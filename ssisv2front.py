import tkinter as tk
from tkinter import *
from tkinter import ttk
import ssisv2back
from tkinter import messagebox

def get_selected_row(event):
    global selected_tuple
    if tree1.selection():

        item = tree1.selection()[0]
        selected_tuple = tree1.item(item)['values']
        clear_entries()
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        sex_value = selected_tuple[2]
        sex_index = sex_options.index(sex_value) if sex_value in sex_options else 0
        sex_combo.current(sex_index)
        year_value = selected_tuple[3]
        year_index = year_options.index(year_value) if year_value in year_options else 0
        year_combo.current(year_index)
        e3.delete(0, END)
        e3.insert(END, selected_tuple[5])
        selected_tuple = None

    if tree2.selection():
        item = tree2.selection()[0]
        selected_tuple = tree2.item(item)['values']
        clear_entries()
        e3.delete(0, END)
        e3.insert(END, selected_tuple[1])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[2])
        selected_tuple = None


def viewstudents_command():
    ''' view_command function to show the output database.
    
    '''
    tree1.delete(*tree1.get_children())  # Clear the treeview
    for row in ssisv2back.view_students():
        tree1.insert('', END, values=row)
    

def viewcourses_command():
    ''' view_command function to show the output database.
    
    '''
    tree2.delete(*tree2.get_children())  # Clear the treeview
    for row in ssisv2back.view_courses():
        tree2.insert('', END, values=row)
    


def search_command():
    tree1.delete(*tree1.get_children())  # Clear the existing items in the tree1 widget


    students = ssisv2back.search(name.get(), id.get(), sex.get(), year.get(), code.get())

    if not students:
        messagebox.showinfo("No Results", "No matching students found.")
        return

    for student in students:
        tree1.insert("", "end", values=student)



def addstudent_command():
    ''' add_command function to add a new student to the database.
    
    '''
    ssisv2back.insert_students(name.get(), id.get(), sex.get(), year.get(),code.get())
    clear_entries()
    viewstudents_command()

def addcourse_command():

    ssisv2back.insert_courses(code.get(),course.get(),)
    clear_entries()
    viewcourses_command()

def updatestudent_command():
    global selected_tuple
    if not tree1.selection():
        messagebox.showwarning("Warning", "No student selected.")
        return
    item = tree1.selection()[0]
    selected_tuple = tree1.item(item)['values']
    if selected_tuple is None:
        messagebox.showwarning("Warning", "No student data selected.")
        return

    confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to update the student's data?")
    if confirmation:
        if not name.get() or not id.get() or not sex.get() or not year.get() or not code.get():
            messagebox.showwarning("Warning", "Please fill in all fields.")
            return
        item = tree1.selection()[0]
        selected_tuple = tree1.item(item)['values']
        ssisv2back.update_students(selected_tuple[0],name.get(), id.get(), sex.get(), year.get(), code.get())
        messagebox.showinfo("Success", "Student data updated successfully.")
        clear_entries()
        viewstudents_command()
    else:
        messagebox.showinfo("Update Canceled", "Update operation canceled.")



def updatecourse_command():
    global selected_tuple
    if not tree2.selection():
        messagebox.showwarning("Warning", "No course selected.")
        return

    # Prompt for user confirmation
    confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to update the course's data?")

    if confirmation:
        item = tree2.selection()[0]
        selected_tuple = tree2.item(item)['values']
        ssisv2back.update_courses(selected_tuple[0], code.get(), course.get())
        clear_entries()
        viewcourses_command()
    else:
        messagebox.showinfo("Update Canceled", "Update operation canceled.")
    

def deletestudent_command():
    ''' deletestudent_command function to delete the data of a specific student.
    
    '''
    if not tree1.selection():
        messagebox.showwarning("Warning", "No student selected.")
        return

    # Prompt for user confirmation
    confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete the student's data?")

    if confirmation:
        item = tree1.selection()[0]
        selected_tuple = tree1.item(item)['values']
        ssisv2back.delete_student(selected_tuple[0])
        clear_entries()
        viewstudents_command()
    else:
        messagebox.showinfo("Deletion Canceled", "Deletion operation canceled.")


def deletecourse_command():
    ''' deletecourse_command function to delete the data of a specific course.
    
    '''
    if not tree2.selection():
        messagebox.showwarning("Warning", "No course selected.")
        return

    # Prompt for user confirmation
    confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete the course's data?")

    if confirmation:
        item = tree2.selection()[0]
        selected_tuple = tree2.item(item)['values']
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
    sex_combo.set('') 
    year_combo.set('')
    e3.delete(0, END)
    e4.delete(0, END)

def clearall():
    clear_entries()
    tree1.selection_remove(tree1.selection())
    tree2.selection_remove(tree2.selection())
    global selected_tuple
    selected_tuple = None

    
def clear_command():
    ''' view_command function to clear content of Listbox.
    
    '''
    tree1.delete(0, END)
    tree2.delete(0, END)
    clear_entries()

# Create the main window
window = Tk()
window.title("Student Information System")
window.resizable(False,False)

name = StringVar()
id = StringVar()
code = StringVar()
course = StringVar()
sex = StringVar()
year = StringVar()

# Create entry fields
e1= ttk.Entry(window,textvariable=name)
e2 = ttk.Entry(window,textvariable= id)
e3 = ttk.Entry(window,textvariable=code)
e4 = ttk.Entry(window,textvariable=course)

sex_options = ['Male', 'Female']
sex_combo = ttk.Combobox(window, textvariable=sex, values=sex_options, state='readonly')

year_options = ['Freshman', 'Sophomore', 'Junior', 'Senior']
year_combo = ttk.Combobox(window, textvariable=year, values=year_options, state='readonly')

# Create labels for entry fields
ttk.Label(window, text="Name:").grid(row=0, column=2, padx=5, pady=5)
ttk.Label(window, text="ID:").grid(row=1, column=2, padx=5, pady=5)
ttk.Label(window, text="Sex:").grid(row=2, column=2, padx=5, pady=5)
ttk.Label(window, text="Year:").grid(row=3, column=2, padx=5, pady=5)
ttk.Label(window, text="Course Code:").grid(row=4, column=2, padx=5, pady=5)
ttk.Label(window, text="Course Name:").grid(row=4, column=4, padx=5, pady=5)

# Position entry fields
e1.grid(row=0, column=3, padx=5, pady=5)
e2.grid(row=1, column=3, padx=5, pady=5)
sex_combo.grid(row=2, column=3, padx=5, pady=5)
year_combo.grid(row=3, column=3, padx=5, pady=5)
e3.grid(row=4, column=3, padx=5, pady=5)
e4.grid(row=4, column=5, padx=5, pady=5)

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
clear_button = ttk.Button(window, text="Clear", command=clearall)
delete_all_button = ttk.Button(window, text="Delete All", command=delete_data_command)
exit_button = ttk.Button(window, text="Exit", command=clear_command)

# Position buttons
view_students_button.grid(row=0, column=4, padx=5, pady=5)
view_courses_button.grid(row=0, column=5, padx=5, pady=5)
add_student_button.grid(row=1, column=4, padx=5, pady=5)
add_course_button.grid(row=1, column=5, padx=5, pady=5)
update_student_button.grid(row=2, column=4, padx=5, pady=5)
update_course_button.grid(row=2, column=5, padx=5, pady=5)
delete_student_button.grid(row=3, column=4, padx=5, pady=5)
delete_course_button.grid(row=3, column=5, padx=5, pady=5)
search_button.grid(row=6, column=2, padx=5, pady=5)
clear_button.grid(row=6, column=3, padx=5, pady=5)
delete_all_button.grid(row=6, column=4, padx=5, pady=5)
exit_button.grid(row=6, column=5, padx=5, pady=5)


# Create Treeview for Database 1
tree1 = ttk.Treeview(window, height=10, columns=('Index','Name', 'ID', 'Sex', 'Year Level', 'Course'), selectmode='extended')
tree1.bind('<<TreeviewSelect>>', get_selected_row)
tree1['show'] = 'headings'
tree1.grid(row=8, column=0, columnspan=4, padx=5, pady=5,sticky="nsew")

# Create scrollbar for Treeview 1
sc1 = ttk.Scrollbar(window, command=tree1.yview)
sc1.grid(row=8, column=4, sticky='ns')

# Configure scrollbar for Treeview 1
tree1.configure(yscrollcommand=sc1.set)

# Add columns to Treeview 1
tree1.heading('Name', text='Name')
tree1.heading('ID', text='ID')
tree1.heading('Sex', text='Sex')
tree1.heading('Year Level', text='Year Level')
tree1.heading('Course', text='Course')

# Set column widths for Treeview 1
tree1.column("Index", width=10)
tree1.column('Name', width=150, minwidth=50, anchor='w')
tree1.column('ID', width=100, minwidth=50, anchor='w')
tree1.column('Sex', width=100, minwidth=50, anchor='w')
tree1.column('Year Level', width=100, minwidth=50, anchor='w')
tree1.column('Course', width=100, minwidth=50, anchor='w')


# Create Treeview for Database 2
tree2 = ttk.Treeview(window, height=10, columns=('Index','Course Code', 'Course Name'), selectmode='extended')
tree2.bind('<<TreeviewSelect>>', get_selected_row)
tree2['show'] = 'headings'
tree2.grid(row=8, column=5, columnspan=2, padx=5, pady=5,sticky="nsew")

# Create scrollbar for Treeview 2
sc2 = ttk.Scrollbar(window, command=tree2.yview)
sc2.grid(row=8, column=8, sticky='ns')

# Configure scrollbar for Treeview 2
tree2.configure(yscrollcommand=sc2.set)

# Add columns to Treeview 2
tree2.heading('Course Code', text='Course Code')
tree2.heading('Course Name', text='Course Name')

# Set column widths for Treeview 2
tree2.column("Index", width=10)
tree2.column('Course Code', width=150, minwidth=50, anchor='w')
tree2.column('Course Name', width=150, minwidth=50, anchor='w')
# Run the main event loop
window.mainloop()


