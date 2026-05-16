import tkinter
from tkinter import ttk, messagebox
import os

window = tkinter.Tk()
window.title("MiniBlog App")
window.geometry("600x750")
window.config(bg="black")

tkinter.Label(text="Username:", bg='black', fg='cyan', font='Cooper 15 bold').grid(row=0,column=0,sticky='w')
tkinter.Label(text="Post Title:", bg='black', fg='cyan', font='Cooper 15 bold').grid(row=1,column=0,sticky='w')
tkinter.Label(text="Post Content:", bg='black', fg='cyan', font='Cooper 15 bold').grid(row=2,column=0,sticky='w')

username_entry = tkinter.Entry(width=30) 
username_entry.grid(row=0, column=1)

title_entry = tkinter.Entry(width=30)
title_entry.grid(row=1, column=1)

content_text = tkinter.Text(width=35, height=10)
content_text.grid(row=2, column=1)

def save_post():
    username = username_entry.get()
    title = title_entry.get()
    content = content_text.get("1.0", "end").strip()

    if username == "" or title == "" or content == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    filename = f"{username}_{title}.txt"

    try:
        with open(filename, "w") as file:
            file.write(f"User: {username}\n")
            file.write(f"Title: {title}\n\n")
            file.write(content)

        messagebox.showinfo("Success", "Post Saved Successfully!")
        load_posts()

    except Exception as e:
        messagebox.showerror("Error", str(e))


def load_posts():
    files = [f for f in os.listdir() if f.endswith(".txt")]
    post_combo['values'] = files

def view_post(event):
    filename = post_combo.get()

    try:
        with open(filename, "r") as file:
            data = file.read()
            display_text.delete("1.0", "end")
            display_text.insert("end", data)

    except:
        messagebox.showerror("Error", "File not found!")

tkinter.Label(text="Saved Posts:", bg='black', fg='yellow', font='Cooper 15 bold').grid(row=3, column=0, sticky='w')

post_combo = ttk.Combobox(width=27)
post_combo.grid(row=3, column=1)
post_combo.bind("<<ComboboxSelected>>", view_post)

display_text = tkinter.Text(width=35, height=10)
display_text.grid(row=4, column=1)

tkinter.Button(text="Save Post",font='Cooper 15 bold',bg='cyan',fg='black',command=save_post).place(x=180, y=520)

load_posts()

window.mainloop()