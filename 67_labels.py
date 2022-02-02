# label =   an area widget that holds text and/or image within a window

from tkinter import *

window = Tk()

photo = PhotoImage(file='dice.png')

label = Label(window,
              text="Hello world",
              font=('Arial', 40, 'bold'),
              fg="green",
              bg="black",
              relief=RAISED,  # border style
              bd=10,  # border-width
              padx=20,
              pady=20,
              image=photo,
              compound='bottom'  # placement of image, relative to the text
              )
label.pack()  # Places the label at default top center position
# label.place(x=0, y=0)

window.mainloop()






