from tkinter import *


def openFile():
    print("File has been opened")


def saveFile():
    print("File has been saved")

def cut():
    print("Cut")


def copy():
    print("Copy")


def paste():
    print("Paste")


window = Tk()

saveImage = PhotoImage(file="save.png")

#  The main bar that holds menus
menubar = Menu(window)
window.config(menu=menubar)

#  Menu-options
fileMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))  # Tearoff is a standard option created which looks like "- - -", we get rid of it
menubar.add_cascade(label="File", menu=fileMenu)  # Drop-down menu 'effect'/visibility
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile, image=saveImage, compound=LEFT)
fileMenu.add_separator()  # Seperator between Open, Save, and Exit
fileMenu.add_command(label="Exit", command=quit)  # Will quit the program

editMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)


window.mainloop()










