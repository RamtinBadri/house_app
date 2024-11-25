from tkinter import *
from tkinter import ttk, IntVar, StringVar
from tkinter.ttk import Treeview

def reset_form():
    id.set(0)
    location.set("")
    postal_code.set(0)
    owner.set("")
    parking.set("")
    elevator.set("")
    roof.set("")



win = Tk()
win.geometry("1000x420")
win.title("house_app")

# id
Label(win, text="id").place(x=20, y=20)
id = IntVar()
Entry(win, textvariable=id).place(x=100, y=20)

# location
Label(win, text="location").place(x=20, y=70)
location = StringVar()
Entry(win, textvariable=location).place(x=100, y=70)

# postal_code
Label(win, text="postal_code").place(x=20, y=120)
postal_code = IntVar()
Entry(win, textvariable=postal_code).place(x=100, y=120)

# owner
Label(win, text="owner").place(x=20, y=170)
owner = StringVar()
Entry(win, textvariable=owner).place(x=100, y=170)

# parking
Label(win, text="parking").place(x=20, y=220)
parking = StringVar()
Entry(win, textvariable=parking).place(x=100, y=220)

# elevator
Label(win, text="elevator").place(x=20, y=270)
elevator = StringVar()
Entry(win, textvariable=elevator).place(x=100, y=270)

# roof
Label(win, text="roof").place(x=20, y=320)
roof = StringVar()
Entry(win, textvariable=roof).place(x=100, y=320)

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
#  Button(win, text="Add", width=8, command=add_click).place(x=80, y=260)

win.mainloop()
