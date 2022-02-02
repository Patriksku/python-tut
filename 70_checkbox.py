from tkinter import *


def display():
    if x.get() == 1:
        print("You agree to everything in all of the documents")
    else:
        print("You have to agree... Or it will not work, do you understand?")


window = Tk()
photo = PhotoImage(file="fraud.png")

x = IntVar()  # Normally the checkbox will return either a 1 or 0, but this can be changed with on/offvalue.
# IntVar (or StringVar etc.) is used in Tkinter.

check_button = Checkbutton(window,
                           text="I agree to the terms and conditions",
                           variable=x,
                           onvalue=1,  # Not needed, these are default 1/0
                           offvalue=0,  # Not needed, these are default 1/0
                           command=display,
                           font=('Arial', 20),
                           fg='green',
                           bg='black',
                           activeforeground='green',
                           activebackground='red',
                           padx=25,
                           pady=10,
                           image=photo,
                           compound=RIGHT)
check_button.pack()
window.mainloop()








