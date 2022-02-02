from tkinter import *
from tkinter import filedialog


def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Projects\\python_fullcourse",
                                    defaultextension=".txt",
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*")
                                    ])
    # Error handling pro
    if file is None:
        return

    filetext = str(text.get(1.0, END))
    # filetext = input("Enter some text to be saved: ")
    file.write(filetext)
    file.close()


window = Tk()

button = Button(window, text="Save", command=saveFile)
button.pack()

text = Text(window)
text.pack()

window.mainloop()





