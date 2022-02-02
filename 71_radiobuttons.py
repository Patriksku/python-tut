from tkinter import *

food = ["Pizza", "Hamburger", "Hotdog"]


def order():
    if x.get() == 0:
        print("You order pizza")
    elif x.get() == 1:
        print("You order a hamburger")
    else:
        print("You order hot dog")


window = Tk()

pizzaImage = PhotoImage(file='food.png')
hamburgerImage = PhotoImage(file='food.png')
hotdogImage = PhotoImage(file='food.png')
foodImages = [pizzaImage, hamburgerImage, hotdogImage]

# variables specified in constructors need to be declared below 'window = Tk()'
x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],
                              variable=x,  # groups radio-buttons together if they share the same variable
                              value=index,
                              padx=25,
                              font=("Impact", 50),
                              image=foodImages[index],
                              compound=RIGHT,
                              indicatoron=0,  # Changes normal circle selections to push-buttons that encompass the imgs
                              width=650,
                              command=order
                              )
    radiobutton.pack(anchor=W)  # Anchor buttons to west

window.mainloop()
