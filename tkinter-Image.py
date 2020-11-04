import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

class Root(Tk)
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Dialog Widget")
        self.minsize(640, 400)

        self.labelFrame = ttk.LabelFrame(self, text='Open a file')
        self.labelFrame.grid(column=0, row=1, padx=20, pady=20)
        self.button()

    def button(self):
        self.button = ttk.Button(self.labelFrame, text='Browse a File',command=self.fileDialog)
        self.button.grid(column=1, row=1)

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir="C:\\Users\\Soundar\\Pictures", title="Select A File", filetype=
        (("jpeg files", "*.jpg"), ("all files", "*.*")))
        self.label = ttk.Label(self.labelFrame, text="")
        self.label.grid(column=1, row=2)
        self.label.configure(text=self.filename)
root=Root()
root.mainloop()


# root = tkinter.Tk()
# root.withdraw() #use to hide tkinter window

# def search_for_file_path ():
#     currdir = os.getcwd()
#     tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
#     if len(tempdir) > 0:
#         print ("You chose: %s" % tempdir)
#     return tempdir
#
#
# file_path_variable = search_for_file_path()
# print ("\nfile_path_variable = ", file_path_variable)
