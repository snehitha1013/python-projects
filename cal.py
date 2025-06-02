
import tkinter as tk

def on_click(value):
    current = display.get()
    if value == "=":
        try:
            result = str(eval(current))
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif value == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, value)


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)
root.configure(bg="#f0f0f0")


display = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="flat", justify="right")
display.pack(padx=10, pady=20, fill="both")


buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]


for row_values in buttons:
    row = tk.Frame(root, bg="#f0f0f0")
    row.pack(expand=True, fill="both")
    for value in row_values:
        button = tk.Button(
            row, text=value, font=("Arial", 18), relief="groove", borderwidth=2,
            command=lambda val=value: on_click(val)
        )
        button.pack(side="left", expand=True, fill="both", padx=2, pady=2)

root.mainloop()
