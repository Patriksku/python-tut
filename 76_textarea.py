# Text widget = functions like a text area, you can enter multiple lines of text
from tkinter import *


def submit():
    input = text.get("1.0", END)  # Index from, Index to
    print(input)


window = Tk()

text = Text(window,
            bg="light yellow",
            font=("Ink Free", 25),  # Text area size corresponds directly with the font size, so window will grow
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg="purple"
            )

text.pack()

button = Button(window, text="Submit", command=submit)
button.pack()


window.mainloop()
















