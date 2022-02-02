from tkinter import *
from tkinter import filedialog


def openFile():
    filePath = filedialog.askopenfilename(initialdir="C:\\Projects\\python_fullcourse",
                                          title="Open file okay?",
                                          # Will initially look for .txt files, but you can choose
                                          # to look for all files as an option on the file-dialog.
                                          filetypes=(("text files", "*.txt"),
                                                     ("all files", "*.*")))
    file = open(filePath, 'r')
    print(file.read())
    file.close()


window = Tk()

button = Button(window, text="Open", command=openFile)
button.pack()

window.mainloop()
