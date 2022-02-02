from tkinter import *
from tkinter import colorchooser  # submodule, therefore we have to import it as well


def click():
    window.config(bg=colorchooser.askcolor()[1])  # index 0 is a tuple of RGB, index 1 is HEXcode for the chosen color


window = Tk()
window.geometry("420x420")
button = Button(window, text="click me", command=click)
button.pack()

window.mainloop()








