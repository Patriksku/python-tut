from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk()  # Instantiate an instance of a window
window.geometry("420x420")
window.title("GUI MUI SHMJUI")

icon = PhotoImage(file='cigjuar.png')
window.iconphoto(True, icon)

window.config(background="green")

window.mainloop()  # Places window on the monitor + listens for events












