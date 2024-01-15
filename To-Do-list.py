import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create and pack widgets
frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, font=("Helvetica", 14))
entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(frame, text="Add Task", command=add_task, font=("Helvetica", 12))
add_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(frame, text="Delete Task", command=delete_task, font=("Helvetica", 12))
delete_button.pack(side=tk.LEFT, padx=5)

listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=("Helvetica", 14))
listbox.pack(pady=10)

# Run the main loop
root.mainloop()
