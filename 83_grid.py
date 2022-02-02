# grid() = geometry manager that organizes widgets in a table-like structure in a parent
from tkinter import *

window = Tk()

titleLabel = Label(window, text="Enter your info", font=("Arial", 25)).grid(row=0, column=0, columnspan=2)

firstNameLabel = Label(window, text="First name: ", width=20, bg="pink").grid(row=1, column=0)  # Width (size) is dependent on the largest widget
                                                                                     # So column will grow bigger
firstNameEntry = Entry(window).grid(row=1, column=1)

lastNameLabel = Label(window, text="Last name: ", bg="pink").grid(row=2, column=0)
lastNameEntry = Entry(window).grid(row=2, column=1)

emailNameLabel = Label(window, text="Email: ", width=30, bg="pink").grid(row=3, column=0)
emailNameEntry = Entry(window).grid(row=3, column=1)

submitButton = Button(window, text="Submit").grid(row=4, column=0, columnspan=2)  # Will span accross 2 columns
                                                                                  # Half of the combined width



window.mainloop()














