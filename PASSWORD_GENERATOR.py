import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        name = name_entry.get()
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Invalid Input", "Password length must be a positive integer.")
            return

        password = generate_password(length)
        password_display.config(text="Generated Password: " + password, fg="blue", font=("Arial", 14, "bold"))
        name_display.config(text="Name: " + name, fg="green", font=("Arial", 12))
        length_display.config(text="Password Length: " + str(length), fg="green", font=("Arial", 12))

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive integer.")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.configure(bg="lightgray")

title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 24, "bold"), fg="purple", bg="lightgray")
title_label.pack(pady=10)

name_label = tk.Label(root, text="Enter your name:", font=("Arial", 12), fg="purple", bg="lightgray")
name_label.pack()

name_entry = tk.Entry(root, width=30, font=("Arial", 12))
name_entry.pack(pady=5)

length_label = tk.Label(root, text="Enter the desired length of the password:", font=("Arial", 12), fg="purple", bg="lightgray")
length_label.pack()

length_entry = tk.Entry(root, width=30, font=("Arial", 12))
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password, font=("Arial", 12), bg="purple", fg="white")
generate_button.pack(pady=10)

name_display = tk.Label(root, text="", font=("Arial", 12), bg="lightgray")
name_display.pack()

length_display = tk.Label(root, text="", font=("Arial", 12), bg="lightgray")
length_display.pack()

password_display = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="lightgray")
password_display.pack()

root.mainloop()
