import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        
        self.tasks = []
        
        # Title Label
        self.title_label = tk.Label(root, text="To-Do List", font=('Helvetica', 18, 'bold'))
        self.title_label.pack(pady=10)
        
        # Task Entry
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)
        
        # Add Task Button
        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)
        
        # Task Listbox
        self.tasks_listbox = tk.Listbox(root, width=50, height=10)
        self.tasks_listbox.pack(pady=10)
        
        # Delete Task Button
        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=5)
        
        # Clear All Tasks Button
        self.clear_all_button = tk.Button(root, text="Clear All Tasks", command=self.clear_all_tasks)
        self.clear_all_button.pack(pady=5)
    
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_tasks_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    
    def delete_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_tasks_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")
    
    def clear_all_tasks(self):
        self.tasks.clear()
        self.update_tasks_listbox()
    
    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
