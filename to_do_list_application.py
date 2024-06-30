import tkinter as tk
from tkinter import messagebox
from tkinter import font

class To_do_App:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        font_style=font.Font(family="Comic Sans MS", size=10, weight="bold")

        # Frame for the task entry and add task button
        self.top_frame = tk.Frame(self.root)
        self.top_frame.pack(pady=10)

        # Entry widget for adding new tasks
        self.task_entry = tk.Entry(self.top_frame, width=45)
        self.task_entry.pack(side=tk.LEFT, padx=(0, 10))

        # Button to add a new task
        self.add_task_button = tk.Button(self.top_frame, text="Add Task", font=font_style, command=self.add_task, bg="#BFEFFF")
        self.add_task_button.pack(side=tk.LEFT)

        # Frame for the listbox and scrollbar
        self.list_frame = tk.Frame(self.root)
        self.list_frame.pack()

        # Scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.list_frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.list_frame, selectmode=tk.MULTIPLE, width=50, height=15, bg="#F5FFFA", yscrollcommand=self.scrollbar.set)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Frame for the delete task and mark as completed buttons
        self.bottom_frame = tk.Frame(self.root)
        self.bottom_frame.pack(pady=10)

        # Button to delete selected tasks
        self.delete_task_button = tk.Button(self.bottom_frame, text="Delete Selected", font=font_style, command=self.delete_task, bg="#FF6A6A")
        self.delete_task_button.pack(side=tk.LEFT, padx=(0, 10))

        # Button to mark selected tasks as completed
        self.mark_completed_button = tk.Button(self.bottom_frame, text="Mark as Completed", font=font_style, command=self.mark_completed, bg="#ADFF2F")
        self.mark_completed_button.pack(side=tk.LEFT)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        selected_tasks = self.task_listbox.curselection()
        for i in selected_tasks[::-1]:  # Reverse the list before deleting
            self.task_listbox.delete(i)
    def mark_completed(self):
        selected_tasks = self.task_listbox.curselection()
        for i in selected_tasks:
            task = self.task_listbox.get(i)
            if not task.startswith("[Completed] "):
                self.task_listbox.delete(i)
                self.task_listbox.insert(i, "[Completed] " + task)
                self.task_listbox.itemconfig(i, {'bg':'light green'})

if __name__ == "__main__":
    root = tk.Tk()
    app = To_do_App(root)
    root.mainloop()
    
