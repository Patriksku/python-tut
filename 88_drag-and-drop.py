from tkinter import *


def drag_start(event):
    widget = event.widget  #  assigns the widget that we are moving to widget, so that the function works across
    #  different widgets.
    # where we click within the label
    widget.startX = event.x
    widget.startY = event.y


def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x  # top right x coordinate of our label relative to the window
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

window = Tk()

label = Label(window, bg="Pink", width=10, height=5)
label.place(x=0, y=0)

label2 = Label(window, bg="Green", width=10, height=5)
label2.place(x=100, y=100)

label.bind("<Button-1>", drag_start)
label.bind("<B1-Motion>", drag_motion)
label2.bind("<Button-1>", drag_start)
label2.bind("<B1-Motion>", drag_motion)

window.mainloop()













