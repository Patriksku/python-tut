from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)  # widget that manages a collection of windows/displays

tab1 = Frame(notebook)  # New frame for tab 1.
tab2 = Frame(notebook)  # New frame for tab 2.

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack(expand=True, fill="both")  # Expand to fill any space not otherwise used.
                                         # fill space on x and y axis (you can specify x and y otherwise)

Label(tab1, text="Hello, this is tab#1", width=50, height=25).pack()
Label(tab2, text="Bye, this is tab#2", width=50, height=25).pack()

window.mainloop()





















