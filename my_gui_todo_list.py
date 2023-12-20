import tkinter as tk
from tkinter import ttk, simpledialog

class List:
    def __init__(self,list):
        self.list = list

    def display_list(self):
        return self.list
    
    def add_task_to_list(self, task):
        self.list.append(task)
    
    def delete_task(self, index):
        if 0 <= index < len(self.list):
            self.list.pop(index)
    
    def edit_task(self, index, edit):
        if 0 <= index < len(self.list):
            self.list[index] = edit

root = tk.Tk()
root.title("Task Manager")

task_list = List([])

def refresh_display():
    listbox.delete(0, tk.END)
    for task in task_list.display_list():
        listbox.insert(tk.END, task)
    task_entry

def add_task():
    task = task_entry.get()
    if task:  # Only add the task if it's not an empty string
        task_list.add_task_to_list(task)
        refresh_display()
        task_entry.delete(0, tk.END)

def edit_task():
    try:
        selected_index = listbox.curselection()[0]
        current_task = listbox.get(selected_index)
        new_task = simpledialog.askstring("Edit Task", "Edit task:", initialvalue=current_task)
        if new_task:
            task_list.edit_task(selected_index, new_task)
            refresh_display
        refresh_display()
    except IndexError:
        pass

def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        task_list.delete_task(selected_index)
        refresh_display()
    except IndexError:
        pass

listbox = tk.Listbox(root)
listbox.pack()

task_entry = ttk.Entry(root)
task_entry.pack()

add_button = ttk.Button(root, text="Add Task", command=add_task)
add_button.pack()

delete_button = ttk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

edit_button = ttk.Button(root, text="Edit Task", command=edit_task)
edit_button.pack()

root.mainloop()