from tkinter import *
from tkinter import messagebox  # import messagebox library


def click():
    # messagebox.showinfo(title="This is an info message box", message="eViL vIruSZZsZ!!!!")
    # while True:
    #     messagebox.showwarning(title="wARNING!", message="eViL vIruSZZsZ!!!!")

    # messagebox.showerror(title="Error!", message="Something went wrong :(")

    # if messagebox.askokcancel(title="ask ok cancel", message="Do you want to do the thing?"):
    #     print("You did the thing.")
    # else:
    #     print("You did NOT do the thing")

    # if messagebox.askretrycancel(title="ask ok cancel", message="Do you want retry the thing?"):
    #     print("You did retry the thing.")
    # else:
    #     print("You did NOT retry the thing")9

    # if messagebox.askyesno(title="yes o no", message="Do you like cake?"):
    #     print("yea.")
    # else:
    #     print("not?!")

    ### This returns a string "yes" or "no", different from the others. ###
    # answer = messagebox.askquestion(title="asking...", message="Do you like pi?")
    # if answer == "yes":
    #     print("3.14")
    # else:
    #     print("you do not like pie?")

    ### This returns True, False, or None -> different from the others as well. ###
    answer = messagebox.askyesnocancel(title="yes no cancelling..", message="Do you like c0de", icon='warning')
    if answer:
        print("nice")
    elif answer == False:
        print("ok.")
    else:
        print("yea cancel like you cancel everything else in life ha?")


window = Tk()

button = Button(window, text="click me", command=click)
button.pack()

window.mainloop()
