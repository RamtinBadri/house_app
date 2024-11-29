from tkinter import *
from tkinter import ttk, IntVar, StringVar
from tkinter.ttk import Treeview
from house_module_validator import *
import tkinter.messagebox as msg  # alias

house_list = []


def reset_form():
    id.set(0)
    location.set("")
    postal_code.set(0)
    owner.set("")
    parking.set("")
    elevator.set("")
    roof.set("")


def add_click():
    if (location_validator(location.get()) and postal_validator(postal_code.get()) and owner_validator(
            owner.get()) and parking_validator(parking.get()) and elevator_validator(elevator.get()) and
            roof_validator(roof.get())):
        house = (location.get(), postal_code.get(), owner.get(), parking.get(), elevator.get(), roof.get())
        table.insert("", END, values=house)
        reset_form()
        msg.showinfo("Save", "Saved Successful")
        house_list.append(house)
    else:
        msg.showerror("Save Error", "Invalid Data !!!")


win = Tk()
win.geometry("1000x420")
win.title("house_app")

# id
Label(win, text="id").place(x=20, y=30)
id = IntVar()
Entry(win, textvariable=id).place(x=100, y=30)

# location
Label(win, text="location").place(x=20, y=80)
location = StringVar()
Entry(win, textvariable=location).place(x=100, y=80)

# postal_code
Label(win, text="postal_code").place(x=20, y=130)
postal_code = IntVar()
Entry(win, textvariable=postal_code).place(x=100, y=130)

# owner
Label(win, text="owner").place(x=20, y=180)
owner = StringVar()
Entry(win, textvariable=owner).place(x=100, y=180)

# parking
Label(win, text="parking").place(x=20, y=230)
parking = StringVar()
Entry(win, textvariable=parking).place(x=100, y=230)

# elevator
Label(win, text="elevator").place(x=20, y=280)
elevator = StringVar()
Entry(win, textvariable=elevator).place(x=100, y=280)

# roof
Label(win, text="roof").place(x=20, y=330)
roof = StringVar()
Entry(win, textvariable=roof).place(x=100, y=330)

# Table
table = Treeview(win, columns=[1, 2, 3, 4, 5, 6, 7], height=15, show="headings")

# Title
table.heading(1, text="id")
table.heading(2, text="location")
table.heading(3, text="postal_code")
table.heading(4, text="owner")
table.heading(5, text="parking")
table.heading(6, text="elevator")
table.heading(7, text="roof")

# Width
table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)
table.column(5, width=100)
table.column(6, width=100)
table.column(7, width=100)
table.place(x=300, y=30)

# Save
Button(win, text="Add", width=10, command=add_click).place(x=200, y=380)

win.mainloop()
