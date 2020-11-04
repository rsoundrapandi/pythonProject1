#importing library
from tkinter import *
from tkinter import ttk

window = Tk()
value=IntVar()
tkvar = StringVar()
#Declaring Window Title
window.title("Registration Screen")
#Declaring Window size
window.geometry('700x700')
#Declaring Window Color
window.configure(background = "black")
#below four fields are declared
Firstname = Label(window ,text = "First Name").grid(row = 0,column = 0)
LastName = Label(window ,text = "Last Name").grid(row = 1,column = 0)
Email = Label(window ,text = "Email Id").grid(row = 2,column = 0)
Mobile = Label(window ,text = "Contact Number").grid(row = 3,column = 0)
EmployeeName=Label(window, text ="Employee Name").grid(row = 4, column = 0)
Gender=Label(window ,text = "Gender Name").grid(row = 5,column = 0)
Languages=Label(window ,text = "Language").grid(row = 6,column = 0)
Label(window, text="Courses").grid(row = 7, column = 0)
Label(window, text="Salary").grid(row = 8, column = 0)
Label(window, text="Employee ID").grid(row = 9, column = 0)
Label(window, text="Email ID").grid(row = 10, column = 0)
Firstname1 = Entry(window).grid(row = 0,column = 1)
Lastname1 = Entry(window).grid(row = 1,column = 1)
Email1 = Entry(window).grid(row = 2,column = 1)
Mobile1 = Entry(window).grid(row = 3,column = 1)
EmployeeName1=Entry(window).grid(row = 4,column = 1)
Gender1 = Radiobutton(window, text="Male", variable =value, value =1).grid(row=5,column=1)
Gender1 = Radiobutton(window, text="Female", variable =value, value =2).grid(row=5,column=2)
Languages=Checkbutton(window, text="English", variable =value ,onvalue = 3, offvalue = 0, height=0,width = 5).grid(row=6,column=1)
Languages=Checkbutton(window, text="Tamil", variable =value ,onvalue = 3, offvalue = 0, height=0,width = 5).grid(row=6,column=2)
choices = { 'Java','C++'}
popupMenu = OptionMenu(window, tkvar, *choices).grid(row=7,column=1)

Salary = Entry(window).grid(row = 8,column = 1)
EmployeeID = Entry(window).grid(row = 9,column = 1)
Email1 = Entry(window).grid(row = 10,column = 1)


def change_dropdown(*args):
    print( tkvar.get() )

#fubction declaration
def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit").grid(row=11,column=0)
window.mainloop()
