import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
        messagebox.showinfo("Success", f"Task '{task}' added successfully.")
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def update_task():
    try:
        selected_index = task_listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task:
            old_task = tasks[selected_index]
            tasks[selected_index] = new_task
            update_listbox()
            task_entry.delete(0, tk.END)
            messagebox.showinfo("Updated", f"Task '{old_task}' updated to '{new_task}'.")
        else:
            messagebox.showwarning("Input Error", "Enter a new task to update.")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to update.")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task = tasks.pop(selected_index)
        update_listbox()
        messagebox.showinfo("Deleted", f"Task '{task}' deleted successfully.")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def view_tasks():
    if tasks:
        all_tasks = "\n".join(tasks)
        messagebox.showinfo("Your Tasks", all_tasks)
    else:
        messagebox.showinfo("Your Tasks", "No tasks available.")

def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# GUI setup
root = tk.Tk()
root.title("Task Management App")
root.geometry("500x450")
root.config(bg="#f0f4f7")

# Title
title_label = tk.Label(root, text="Task Management App", font=("Helvetica", 18, "bold"), bg="#992b8c", fg="white", pady=10)
title_label.pack(fill="x")

# Task Entry
task_entry = tk.Entry(root, width=40, font=("Arial", 12), bd=2, relief="solid")
task_entry.pack(pady=10)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#f0f4f7")
btn_frame.pack(pady=5)

btn_style = {"width": 15, "height": 1, "font": ("Arial", 11, "bold"), "relief": "raised", "bd": 2}

add_btn = tk.Button(btn_frame, text="➕ Add Task", bg="#27ae60", fg="white", command=add_task, **btn_style)
add_btn.grid(row=0, column=0, padx=5, pady=5)

update_btn = tk.Button(btn_frame, text="✏️ Update Task", bg="#f312c6", fg="white", command=update_task, **btn_style)
update_btn.grid(row=0, column=1, padx=5, pady=5)

delete_btn = tk.Button(btn_frame, text="🗑️ Delete Task", bg="#e74c3c", fg="white", command=delete_task, **btn_style)
delete_btn.grid(row=1, column=0, padx=5, pady=5)

view_btn = tk.Button(btn_frame, text="📋 View Tasks", bg="#2980b9", fg="white", command=view_tasks, **btn_style)
view_btn.grid(row=1, column=1, padx=5, pady=5)

# Task List with Scrollbar
list_frame = tk.Frame(root, bg="#f0f4f7")
list_frame.pack(pady=10)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox = tk.Listbox(list_frame, width=60, height=12, font=("Arial", 12), yscrollcommand=scrollbar.set, bd=2, relief="solid", selectbackground="#3498db", selectforeground="white")
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar.config(command=task_listbox.yview)

root.mainloop()
