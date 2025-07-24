import tkinter as tk
from tkinter import ttk, messagebox

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0:
        return "😥 Oops! Can't divide by zero."
    return a / b


def clear_placeholder(event, entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, tk.END)
        entry.config(fg='black')


def restore_placeholder(event, entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.config(fg='grey')

def calculate():
    try:
        a_text = entry1.get()
        b_text = entry2.get()

        if a_text in [entry1_placeholder, ""] or b_text in [entry2_placeholder, ""]:
            messagebox.showwarning("🧐 Hold on", "Please enter both numbers before calculating.")
            return

        a = float(a_text)
        b = float(b_text)
        op = operation_var.get()

        if op == "Add":
            result = add(a, b)
            message = f"✅ Alright! The sum is: {result}"
        elif op == "Subtract":
            result = sub(a, b)
            message = f"📉 Got it! The difference is: {result}"
        elif op == "Multiply":
            result = mul(a, b)
            message = f"✖️ Boom! The product is: {result}"
        elif op == "Divide":
            result = div(a, b)
            message = f"➗ Here's your division result: {result}"
        else:
            message = "❓ Something went wrong."

        result_label.config(text=message)
    except ValueError:
        messagebox.showerror("😵 Invalid Input", "Oops! Please enter valid numbers only.")


root = tk.Tk()
root.title("🤝 Friendly Calculator")
root.geometry("430x470")
root.configure(bg="#f7f7f7")


tk.Label(root, text="👋 Hello! I'm your friendly calculator assistant.", font=("Helvetica", 13, "bold"), bg="#f7f7f7").pack(pady=12)
tk.Label(root, text="Let me help you with some quick math!", font=("Helvetica", 11), bg="#f7f7f7").pack(pady=4)

entry1_placeholder = "👉 Type your first number here..."
entry2_placeholder = "👉 Now your second number please..."


entry1 = tk.Entry(root, font=("Helvetica", 12), fg='grey', justify='center', width=30)
entry1.insert(0, entry1_placeholder)
entry1.bind("<FocusIn>", lambda event: clear_placeholder(event, entry1, entry1_placeholder))
entry1.bind("<FocusOut>", lambda event: restore_placeholder(event, entry1, entry1_placeholder))
entry1.pack(pady=10)


entry2 = tk.Entry(root, font=("Helvetica", 12), fg='grey', justify='center', width=30)
entry2.insert(0, entry2_placeholder)
entry2.bind("<FocusIn>", lambda event: clear_placeholder(event, entry2, entry2_placeholder))
entry2.bind("<FocusOut>", lambda event: restore_placeholder(event, entry2, entry2_placeholder))
entry2.pack(pady=10)


tk.Label(root, text="🛠️ What do you want me to do?", font=("Helvetica", 11), bg="#f7f7f7").pack(pady=5)
operation_var = tk.StringVar(value="Add")
operation_dropdown = ttk.Combobox(root, textvariable=operation_var, values=["Add", "Subtract", "Multiply", "Divide"], font=("Helvetica", 11), state="readonly", width=25)
operation_dropdown.pack(pady=10)

tk.Button(root, text="✨ Let's Calculate!", font=("Helvetica", 12, "bold"), bg="#5cb85c", fg="white", command=calculate).pack(pady=15)

result_label = tk.Label(root, text="", font=("Helvetica", 13), bg="#f7f7f7", wraplength=350, justify="center", fg="#333")
result_label.pack(pady=20)
def goodbye():
    messagebox.showinfo("Bye Bye 👋", "Thanks for using the calculator. Have a nice day! 🌈")
    root.destroy()

tk.Button(root, text="Exit 😌", font=("Helvetica", 10), bg="#e74c3c", fg="white", command=goodbye).pack(pady=10)

root.mainloop()
