import tkinter as tk
from tkinter import messagebox

tasks = {}

def add_task():
    task_id = task_id_entry.get()
    task_description = task_description_entry.get()

    if task_id and task_description:
        tasks[task_id] = task_description
        update_listbox()
        task_id_entry.delete(0, tk.END)
        task_description_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter both task ID and description.")

def update_listbox():
    task_listbox.delete(0, tk.END)
    for task_id, task_description in tasks.items():
        task_listbox.insert(tk.END, f"{task_id}. {task_description}")

def edit_task():
    selected_task = task_listbox.get(tk.ACTIVE)
    if selected_task:
        task_id, task_description = selected_task.split('.', 1)
        task_id_entry.delete(0, tk.END)
        task_id_entry.insert(tk.END, task_id)
        task_description_entry.delete(0, tk.END)
        task_description_entry.insert(tk.END, task_description)

def save_task():
    selected_task = task_listbox.get(tk.ACTIVE)
    if selected_task:
        task_id, _ = selected_task.split('.', 1)
        updated_description = task_description_entry.get()
        tasks[task_id] = updated_description
        update_listbox()
        task_id_entry.delete(0, tk.END)
        task_description_entry.delete(0, tk.END)

def delete_task():
    selected_task = task_listbox.get(tk.ACTIVE)
    if selected_task:
        task_id, _ = selected_task.split('.', 1)
        del tasks[task_id]
        update_listbox()

def main():
    global task_id_entry
    global task_description_entry
    global task_listbox

    root = tk.Tk()
    root.title("To-Do List Application")
    root.geometry("400x500")

    root.configure(bg="#f0f0f0")
    root.option_add("*Font", "Arial 12")

    task_frame = tk.Frame(root, bg="#ffffff")
    task_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    task_id_label = tk.Label(task_frame, text="Task ID:", bg="#ffffff")
    task_id_label.grid(row=0, column=0, padx=5, pady=5)

    task_id_entry = tk.Entry(task_frame)
    task_id_entry.grid(row=0, column=1, padx=5, pady=5)

    task_description_label = tk.Label(task_frame, text="Task Description:", bg="#ffffff")
    task_description_label.grid(row=1, column=0, padx=5, pady=5)

    task_description_entry = tk.Entry(task_frame)
    task_description_entry.grid(row=1, column=1, padx=5, pady=5)

    add_button = tk.Button(task_frame, text="Add", command=add_task, bg="#90ee90", width=10)
    add_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

    edit_button = tk.Button(task_frame, text="Edit", command=edit_task, bg="#87ceeb", width=10)
    edit_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    save_button = tk.Button(task_frame, text="Save", command=save_task, bg="#ffa500", width=10)
    save_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    delete_button = tk.Button(task_frame, text="Delete", command=delete_task, bg="#ff6347", width=10)
    delete_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    task_listbox = tk.Listbox(task_frame, selectmode=tk.SINGLE)
    task_listbox.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

    update_listbox()

    root.mainloop()

if __name__ == "__main__":
    main()
