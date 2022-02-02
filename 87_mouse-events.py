from tkinter import *


def doSomething(event):
    print("You did it", str(event.x) + "," + str(event.y))


window = Tk()

# window.bind("<Button-1>", doSomething) # left mouse click
# window.bind("<Button-2>", doSomething) # scroll wheel click
# window.bind("<Button-3>", doSomething) # right mouse click
# window.bind("<ButtonRelease>", doSomething)
# window.bind("<Enter>", doSomething)  # position of entering the GUI window
# window.bind("<Leave>", doSomething)  # position of leaving the GUI window
window.bind("<Motion>", doSomething)  # Where the mouse moved

window.mainloop()





