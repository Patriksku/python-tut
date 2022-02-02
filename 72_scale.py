from tkinter import *

def submit():
    print("The temperature is:", scale.get(), "degrees C")


window = Tk()

# This will spawn above the scale as the label will be created before scale, and vice versa for cold.
# hot = PhotoImage(file='hot.png')
# hotLabel = Label(image=hot)
# hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,  # Default
              font=("Consolas", 20),
              tickinterval=10,  # Numerical tick-indicators on the scale
              # showvalue=FALSE,  # Hide current value
              resolution=5,  # Increment for each movement of the scale
              troughcolor='#69EAFF',  # "bg" color of the scale below the scale icon
              fg='#FF1C00',
              bg='black'
              )

# scale.set(100)  # Set default value of scale
scale.set(((scale['from'] - scale['to']) / 2) + scale['to'])  # Little formula to always set it to the middle
scale.pack()

cold = PhotoImage(file='cold.png')
coldLabel = Label(image=cold)
coldLabel.pack()

button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()





