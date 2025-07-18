
import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(str(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, font="Arial 20")
entry.pack(pady=10, fill=tk.X, padx=10)

buttons = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["C", "0", "=", "/"]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack()
    for b in row:
        btn = tk.Button(frame, text=b, font="Arial 18", width=4, command=lambda x=b: click(tk.Event(widget=btn)))
        btn.bind("<Button-1>", click)
        btn.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()
