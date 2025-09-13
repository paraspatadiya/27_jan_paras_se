import tkinter as tk
from tkinter import messagebox
import re

# ------------------ Classes ------------------
class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class Device:
    def __init__(self, model, issue):
        self.model = model
        self.issue = issue

class Repair:
    def __init__(self, customer, device, technician):
        self.customer = customer
        self.device = device
        self.technician = technician
        self.status = "Pending"

# ------------------ File Save ------------------
def save(text):
    try:
        with open("repair.txt", "a") as f:
            f.write(text + "\n")
    except Exception as e:
        messagebox.showerror("Error", f"File error: {e}")

# ------------------ Add Customer ------------------
def add_customer():
    name = entry_name.get()
    phone = entry_phone.get()
    model = entry_model.get()
    issue = entry_issue.get()
    tech = entry_technician.get()

    if name == "" or phone == "" or model == "" or issue == "":
        messagebox.showwarning("Warning", "All fields are required")
        return

    try:
        c = Customer(name, phone)
        d = Device(model, issue)
        r = Repair(c, d, tech)

        record = f"{c.name},{c.phone},{d.model},{d.issue},{r.technician},{r.status}"
        save(record)

        messagebox.showinfo("Success", "Repair order added!")

        # clear fields
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_model.delete(0, tk.END)
        entry_issue.delete(0, tk.END)
        entry_technician.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

# ------------------ Search Orders ------------------
def search_orders():
    key = entry_search.get()
    if key == "":
        messagebox.showwarning("Warning", "Enter a keyword to search")
        return
    try:
        with open("repair.txt", "r") as f:
            data = f.readlines()
        results = []
        for line in data:
            if re.search(key, line, re.IGNORECASE):
                results.append(line.strip())

        if results:
            messagebox.showinfo("Search Results", "\n".join(results))
        else:
            messagebox.showinfo("Search Results", "No matches found!")
    except FileNotFoundError:
        messagebox.showerror("Error", "No records found!")

# ------------------ Billing ------------------
def generate_bill():
    try:
        parts = float(entry_parts.get())
        service = float(entry_service.get())
        tax = (parts + service) * 0.18
        total = parts + service + tax
        messagebox.showinfo("Bill", f"Parts: {parts}\nService: {service}\nTax: {tax}\nTotal: {total}")

        save(f"BILL -> Parts:{parts}, Service:{service}, Tax:{tax}, Total:{total}")

        entry_parts.delete(0, tk.END)
        entry_service.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers for billing!")

# ------------------ GUI ------------------
root = tk.Tk()
root.title("Tech Repair || Welcome")
root.geometry("600x800")

tk.Label(root, text="Customer Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Phone").pack()
entry_phone = tk.Entry(root)
entry_phone.pack()

tk.Label(root, text="Device Model").pack()
entry_model = tk.Entry(root)
entry_model.pack()

tk.Label(root, text="Issue").pack()
entry_issue = tk.Entry(root)
entry_issue.pack()

tk.Label(root, text="Technician").pack()
entry_technician = tk.Entry(root)
entry_technician.pack()

tk.Button(root, text="Add Repair Order", command=add_customer).pack(pady=5)

tk.Label(root, text="Search Orders (enter your phone number)").pack()
entry_search = tk.Entry(root)
entry_search.pack()
tk.Button(root, text="Search", command=search_orders).pack(pady=5)

tk.Label(root, text="Billing").pack()
tk.Label(root, text="Parts Cost").pack()
entry_parts = tk.Entry(root)
entry_parts.pack()
tk.Label(root, text="Service Cost").pack()
entry_service = tk.Entry(root)
entry_service.pack()
tk.Button(root, text="Generate Bill", command=generate_bill).pack(pady=5)

root.mainloop()
