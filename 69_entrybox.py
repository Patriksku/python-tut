# Entry widget = textbox that accepts a single line of user input

from tkinter import *


def submit():
    username = entry.get()
    print("Hello", username)
    entry.config(state=DISABLED)


def delete():
    entry.delete(0, END)  # Delete all characters in the entry-box from index 0 to END


def backspace():
    entry.delete(len(entry.get())-1, END)


window = Tk()

entry = Entry(window,
              font=("Arial", 50),
              fg="green",
              bg="black",
              show="*")  # Text will now be shown as '*'
# entry.insert(0, 'Spongebob')  # Insert default text at 0 index
entry.pack(side=LEFT)

submit_button = Button(window, text="Submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="Delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="Backspace", command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()
