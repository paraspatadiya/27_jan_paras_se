import tkinter
from tkinter import ttk, messagebox
import os
from datetime import datetime

window = tkinter.Tk()
window.title("RepairMate Beginner - One Save Button")
window.geometry("400x650")
window.config(bg="lightyellow")


CUSTOMERS_FILE = "customers.txt"
DEVICES_FILE = "devices.txt"
REPAIRS_FILE = "repairs.txt"

for f in (CUSTOMERS_FILE, DEVICES_FILE, REPAIRS_FILE):
    if not os.path.exists(f):
        open(f, "a").close()

def write_line(fname, line):
    with open(fname, "a", encoding="utf-8") as file:
        file.write(line + "\n")


tkinter.Label(text="Customer Name:", bg="lightyellow", fg="red",font="Cooper 13 bold").grid(row=0, column=0, sticky='w')
entry_cust = tkinter.Entry()
entry_cust.grid(row=0, column=1)

tkinter.Label(text="Phone:", bg="lightyellow", fg="red",font="Cooper 13 bold").grid(row=1, column=0, sticky='w')
entry_phone = tkinter.Entry()
entry_phone.grid(row=1, column=1)


tkinter.Label(text="Device Brand:", bg="lightyellow", fg="red",font="Cooper 13 bold").grid(row=3, column=0, sticky='w')

brands = ["Samsung", "iPhone", "Vivo", "Oppo", "Realme", "OnePlus", "Xiaomi"]
brand_combo = ttk.Combobox(values=brands)
brand_combo.grid(row=3, column=1)

tkinter.Label(text="Model Name:", bg="lightyellow", fg="red",font="Cooper 13 bold").grid(row=4, column=0, sticky='w')
entry_model = tkinter.Entry()
entry_model.grid(row=4, column=1)

tkinter.Label(text="Serial Number:", bg="lightyellow", fg="red",font="Cooper 13 bold").grid(row=5, column=0, sticky='w')
entry_serial = tkinter.Entry()
entry_serial.grid(row=5, column=1)


tkinter.Label(text="Issue:", bg="lightyellow", fg="red",font="Cooper 13 bold").grid(row=7, column=0, sticky='w')
entry_issue = tkinter.Entry()
entry_issue.grid(row=7, column=1)

tkinter.Label(text="Technician Name:", bg="lightyellow", fg="red",font="Cooper 13 bold").grid(row=8, column=0, sticky='w')
entry_tech = tkinter.Entry()
entry_tech.grid(row=8, column=1)

tkinter.Label(text="Status:", bg="lightyellow", fg="red",font="Cooper 13 bold").grid(row=9, column=0, sticky='w')

statuses = ["Pending", "In Progress", "Completed"]
status_combo = ttk.Combobox(values=statuses)
status_combo.grid(row=9, column=1)


def save_all():
    name = entry_cust.get()
    phone = entry_phone.get()
    brand = brand_combo.get()
    model = entry_model.get()
    serial = entry_serial.get()
    issue = entry_issue.get()
    tech = entry_tech.get()
    status = status_combo.get()

    if name == "" or phone == "" or brand == "" or model == "" or serial == "" or issue == "" or tech == "" or status == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    write_line(CUSTOMERS_FILE, name + "|" + phone)
    write_line(DEVICES_FILE, brand + "|" + model + "|" + serial + "|" + name)
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    write_line(REPAIRS_FILE, model + "|" + issue + "|" + tech + "|" + status + "|" + time)

    messagebox.showinfo("Saved", "Everything Saved Successfully!")


tkinter.Button(text="SAVE ALL", font="Cooper 15 bold",bg="white", fg="red", command=save_all).place(x=130, y=580)

window.mainloop()
