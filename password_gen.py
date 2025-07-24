import random
import string
import tkinter as tk
from tkinter import messagebox


def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Too Short", "🔒 Password should be at least 4 characters long.")
            return

        chars = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(chars) for _ in range(length))
        password_display.config(state='normal')
        password_display.delete(0, tk.END)
        password_display.insert(0, password)
        password_display.config(state='readonly')
    except ValueError:
        messagebox.showerror("Invalid Input", "❌ Please enter a valid number.")

root = tk.Tk()
root.title("🔐 Friendly Password Generator")
root.geometry("400x300")
root.config(bg="#f4f4f4")


welcome_label = tk.Label(root, text="👋 Hello! Let's generate a strong password for you.", font=("Helvetica", 12), bg="#f4f4f4")
welcome_label.pack(pady=20)


length_label = tk.Label(root, text="Enter desired password length:", font=("Helvetica", 11), bg="#f4f4f4")
length_label.pack()

length_entry = tk.Entry(root, font=("Helvetica", 12), width=10, justify='center')
length_entry.pack(pady=5)


generate_button = tk.Button(root, text="🔁 Generate Password", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=generate_password)
generate_button.pack(pady=10)

password_display = tk.Entry(root, font=("Helvetica", 12), width=30, justify='center', state='readonly')
password_display.pack(pady=10)


exit_button = tk.Button(root, text="Exit ❌", font=("Helvetica", 10), bg="#ff4d4d", fg="white", command=root.quit)
exit_button.pack(pady=10)

root.mainloop()
