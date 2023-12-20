import tkinter as tk
from tkinter import simpledialog

# Assuming the List class and its methods from your script
class List:
    def __init__(self, list):
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

# GUI application class
class TodoListApp:
    def __init__(self, master):
        self.master = master
        master.title("Todo List")

        self.list = List([])
        
        self.listbox = tk.Listbox(master)
        self.listbox.pack()

        self.entry_task = tk.Entry(master)
        self.entry_task.pack()

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        self.edit_button = tk.Button(master, text="Edit Task", command=self.edit_task)
        self.edit_button.pack()

        self.refresh_list()

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for task in self.list.display_list():
            self.listbox.insert(tk.END, task)

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.list.add_task_to_list(task)
            self.refresh_list()
            self.entry_task.delete(0, tk.END)

    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            self.list.delete_task(index)
            self.refresh_list()
        except IndexError:
            pass

    def edit_task(self):
        try:
            index = self.listbox.curselection()[0]
            task = self.list.display_list()[index]
            new_task = simpledialog.askstring("Edit Task", "Edit task:", initialvalue=task)
            if new_task:
                self.list.edit_task(index, new_task)
                self.refresh_list()
        except IndexError:
            pass

# Main function to run the application
def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

# Run the application
if __name__ == "__main__":
    main()
