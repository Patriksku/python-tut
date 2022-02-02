from tkinter import *
import time

WIDTH = 500
HEIGHT = 500
xVelocity = 3
yVelocity = 2


window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

bgImage = PhotoImage(file='woods.png')
myBgImage = canvas.create_image(0, 0, image=bgImage, anchor=NW)

photoImage = PhotoImage(file='shoot.png')
myImage = canvas.create_image(0, 0, image=photoImage, anchor=NW)

image_width = photoImage.width()
image_height = photoImage.height()

while True:
    coordinates = canvas.coords(myImage)
    print(coordinates)

    if coordinates[0] >= (WIDTH - image_width) or coordinates[0] < 0:
        xVelocity = -xVelocity

    if coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0:
        yVelocity = -yVelocity

    canvas.move(myImage, xVelocity, yVelocity)
    window.update()
    time.sleep(0.01)


window.mainloop()











