
import tkinter as tk
import string
import random

def generate():
    length = int(length_entry.get())
    chars = string.ascii_letters
    if digits_var.get():
        chars += string.digits
    if special_var.get():
        chars += string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    output.delete(0, tk.END)
    output.insert(0, password)

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Length:").pack()
length_entry = tk.Entry(root)
length_entry.insert(0, "12")
length_entry.pack()

digits_var = tk.IntVar()
special_var = tk.IntVar()
tk.Checkbutton(root, text="Include Digits", variable=digits_var).pack()
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).pack()

tk.Button(root, text="Generate Password", command=generate).pack(pady=10)
output = tk.Entry(root, width=30)
output.pack()

root.mainloop()
