# listbox = A listing of selectable text items within it's own container

from tkinter import *


def submit():
    food = []

    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    for item in food:
        print("You have ordered:", item)


def add():
    listbox.insert(listbox.size(),  # At the last index of the current listbox size
                   entryBox.get())
    listbox.config(height=listbox.size())  # Adjust height of listbox


def delete():
    if listbox.curselection() != ():

        # Reversed, because when we delete multiple items, the amount of elements, and thus indexes, change.
        # So if we delete items in reversed order, the indexes of the items that are left, are not affected.
        for index in reversed(listbox.curselection()):
            listbox.delete(index)

        listbox.config(height=listbox.size())  # Adjust height of listbox


window = Tk()

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia", 35),
                  width=12,
                  selectmode=MULTIPLE)  # Select multiple items
listbox.pack()

listbox.insert(1, "pizza")
listbox.insert(2, "pasta")
listbox.insert(3, "garlic bread")
listbox.insert(4, "soup")
listbox.insert(5, "salad")

listbox.config(height=listbox.size())  # Will dynamically adjust the height of the listbox

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window, text="Add", command=add)
submitButton.pack()

addButton = Button(window, text="Submit", command=submit)
addButton.pack()

deleteButton = Button(window, text="Delete", command=delete)
deleteButton.pack()



window.mainloop()
