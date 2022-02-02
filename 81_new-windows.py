from tkinter import *


def create_window():
    # dependent on bottom window, so if bottom window closes, this also closes
    # new_window = Toplevel()  # new window 'on top' of other windows, linked to a 'bottom' window

    new_window = Tk()  # new independent window
    old_window.destroy()  # close old window when creating new window

old_window = Tk()

Button(old_window, text="Create new window", command=create_window).pack()

old_window.mainloop()







