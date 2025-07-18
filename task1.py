# gui_todo.py
import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_list()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Entry", "Please enter a task.")

def update_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        update_list()
    except IndexError:
        messagebox.showwarning("No Selection", "Please select a task to delete.")

# UI Setup
root = tk.Tk()
root.title("To-Do List App")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

tk.Button(root, text="Add Task", command=add_task).pack()
tk.Button(root, text="Delete Task", command=delete_task).pack()

listbox = tk.Listbox(root, width=40)
listbox.pack(pady=10)

root.mainloop()
