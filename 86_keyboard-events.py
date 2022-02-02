from tkinter import *


def doSomething(event):
    label.config(text=event.keysym)


window = Tk()


window.bind("<Key>", doSomething)  # 'Key' will respond to all keys, otherwise you can specify like 'q'

label = Label(window, font=("Arial", 38))
label.pack()

window.mainloop()







