from tkinter import *

count = 0


def click():
    #  Python thinks that any name assigned within a function is local, unless told otherwise
    #  You want to avoid using 'global'
    global count  # For it to be accessible from the function
    count += 1
    print("You clicked the button... " + str(count), "times.")


window = Tk()
photo = PhotoImage(file="dice.png")

button = Button(window,
                text="Click me",
                command=click,  # This is a callback
                font=("Comic Sans", 30),
                fg="red",
                bg="black",
                # button will change color when you click, so we have to change the active fg and bg
                activeforeground="red",
                activebackground="black",
                state=ACTIVE,  # DISABLED to deactivate button
                image=photo,
                compound="bottom"
                )
button.pack()

window.mainloop()
