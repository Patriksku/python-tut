from tkinter import *

# --------------------------------------------------------
# move images on WINDOW
# --------------------------------------------------------
# def moveUp(event):
#     label.place(x=label.winfo_x(), y=label.winfo_y()-5)
#
#
# def moveDown(event):
#     label.place(x=label.winfo_x(), y=label.winfo_y()+5)
#
#
# def moveLeft(event):
#     label.place(x=label.winfo_x()-5, y=label.winfo_y())
#
#
# def moveRight(event):
#     label.place(x=label.winfo_x()+5, y=label.winfo_y())
#
#
# window = Tk()
# window.geometry("500x500")
#
# window.bind("<w>", moveUp)
# window.bind("<s>", moveDown)
# window.bind("<a>", moveLeft)
# window.bind("<d>", moveRight)
# window.bind("<Up>", moveUp)
# window.bind("<Down>", moveDown)
# window.bind("<Left>", moveLeft)
# window.bind("<Right>", moveRight)
#
# myImage = PhotoImage(file="shoot.png")
# label = Label(window, image=myImage)
# label.place(x=220, y=220)
#
# window.mainloop()


# --------------------------------------------------------
# move images on CANVAS
# --------------------------------------------------------
def moveUp(event):
    canvas.move(canvasPhoto, 0, -10)  # How many pixels we want to move along x- and y-axis


def moveDown(event):
    canvas.move(canvasPhoto, 0, 10)


def moveLeft(event):
    canvas.move(canvasPhoto, -10, 0)


def moveRight(event):
    canvas.move(canvasPhoto, 10, 0)


window = Tk()

window.bind("<w>", moveUp)
window.bind("<s>", moveDown)
window.bind("<a>", moveLeft)
window.bind("<d>", moveRight)

canvas = Canvas(window, width=500, height=500)
canvas.pack()

myImage = PhotoImage(file="shoot.png")
canvasPhoto = canvas.create_image(0, 0, image=myImage, anchor=NW)

window.mainloop()








