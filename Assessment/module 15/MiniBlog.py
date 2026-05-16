import tkinter
from tkinter import ttk, messagebox
import os

window = tkinter.Tk()
window.title("MiniBlog")
window.geometry("500x600")
window.config(bg="lightblue")

tkinter.Label(text="Username:", bg='lightblue', fg='red', font='Cooper 12 bold').grid(row=0, column=0, sticky='w')
tkinter.Label(text="Title:", bg='lightblue', fg='red', font='Cooper 12 bold').grid(row=1, column=0, sticky='w')
tkinter.Label(text="Content:", bg='lightblue', fg='red', font='Cooper 12 bold').grid(row=2, column=0, sticky='nw')

username_entry = tkinter.Entry(width=30)
username_entry.grid(row=0, column=1)

title_entry = tkinter.Entry(width=30)
title_entry.grid(row=1, column=1)

content_text = tkinter.Text(width=30, height=10)
content_text.grid(row=2, column=1)

tkinter.Label(text="View Posts:", bg='lightblue', fg='red', font='Cooper 12 bold').grid(row=3, column=0, sticky='w')

post_list = ttk.Combobox(width=28)
post_list.grid(row=3, column=1)

def save_post():
    username = username_entry.get()
    title = title_entry.get()
    content = content_text.get("1.0", tkinter.END)

    if username == "" or title == "" or content.strip() == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    filename = username + "_" + title + ".txt"

    try:
        file = open(filename, "w")
        file.write("Username: " + username + "\n")
        file.write("Title: " + title + "\n")
        file.write("Content:\n" + content)
        file.close()

        messagebox.showinfo("Success", "Post Saved Successfully!")
        load_posts()

    except Exception as e:
        messagebox.showerror("Error", str(e))


def load_posts():
    files = [f for f in os.listdir() if f.endswith(".txt")]
    post_list['values'] = files


def view_post():
    selected = post_list.get()

    if selected == "":
        messagebox.showwarning("Warning", "Select a post first!")
        return

    try:
        file = open(selected, "r")
        data = file.read()
        file.close()

        content_text.delete("1.0", tkinter.END)
        content_text.insert(tkinter.END, data)

    except:
        messagebox.showerror("Error", "File not found!")


tkinter.Button(text="Save Post", font='Cooper 12 bold', command=save_post).place(x=100, y=400)

tkinter.Button(text="View Post", font='Cooper 12 bold', command=view_post).place(x=250, y=400)

# Load existing posts on start
load_posts()

window.mainloop()