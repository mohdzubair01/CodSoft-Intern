import tkinter as tk
from tkinter import messagebox

def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        result_label.config(text="Result: {:.2f}".format(result))
    except Exception as e:
        result_label.config(text="Error: " + str(e))

def clear():
    entry.delete(0, tk.END)
    result_label.config(text="Result: ") 
    
root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, font=("Arial", 16), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

result_label = tk.Label(root, text="Result: ", font=("Arial", 16))
result_label.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+'
]

row, col = 2, 0
for button_text in button_texts:
    tk.Button(root, text=button_text, font=("Arial", 16), width=5, height=2,
              command=lambda text=button_text: entry.insert(tk.END, text)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text='C', font=("Arial", 16), width=5, height=2,
          command=clear).grid(row=row, column=3, padx=5, pady=5)

tk.Button(root, text='=', font=("Arial", 16), width=5, height=2,
          command=calculate).grid(row=row+1, column=2, padx=5, pady=5)

root.configure(bg="#f0f0f0")
root.option_add("*Font", "Arial 16")

root.mainloop()
