import tkinter as tk
import math

# Makes le window :0
root = tk.Tk()
root.title("Golden Calculator")
root.geometry("350x500")
root.configure(bg="#B8860B")  # Dark goldenrod background

# Entry for input n output
entry = tk.Entry(root, width=20, font=("Arial", 24), bd=5, relief="ridge",
                 justify="right", bg="#FFF8DC", fg="black")  # Cornsilk input box
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)


# Function that does the button click
def click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + symbol)

# Clear function
def clear():
    entry.delete(0, tk.END)

# Backspace function
def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

# Equals function
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error (÷0)")
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Square root
def square_root():
    try:
        num = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(math.sqrt(num)))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Square
def square():
    try:
        num = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(num * num))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Modulus
def modulus():
    click("%")


# Button layout and added parenthesis for operations like PEMDAS :3
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), ("√", 1, 4),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3), ("x²", 2, 4),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3), ("%", 3, 4),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3), ("⌫", 4, 4),
    ("(", 5, 0), (")", 5, 1)
]

# Create buttons with more of cool gold look 
for (text, row, col) in buttons:
    if text == "=":
        b = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18),
                      bg="#DAA520", fg="white", activebackground="#CD950C",
                      command=calculate)
    elif text == "√":
        b = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18),
                      bg="#DAA520", fg="white", activebackground="#CD950C",
                      command=square_root)
    elif text == "x²":
        b = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18),
                      bg="#DAA520", fg="white", activebackground="#CD950C",
                      command=square)
    elif text == "%":
        b = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18),
                      bg="#DAA520", fg="white", activebackground="#CD950C",
                      command=modulus)
    elif text == "⌫":
        b = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18),
                      bg="#DAA520", fg="white", activebackground="#CD950C",
                      command=backspace)
    else:
        b = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18),
                      bg="#DAA520", fg="white", activebackground="#CD950C",
                      command=lambda t=text: click(t))
    b.grid(row=row, column=col, padx=5, pady=5)

# Clear button (big at bottom, darker gold)
clear_btn = tk.Button(root, text="C", width=15, height=2, font=("Arial", 18),
                      bg="#8B7500", fg="white", activebackground="#CD950C",
                      command=clear)
clear_btn.grid(row=5, column=2, columnspan=3, padx=5, pady=5)

# Runs the app yay!
root.mainloop()

