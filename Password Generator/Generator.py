import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    length = int(length_entry.get())
    include_uppercase = uppercase_var.get()
    include_lowercase = lowercase_var.get()
    include_numbers = numbers_var.get()
    include_symbols = symbols_var.get()

    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not any([include_uppercase, include_lowercase, include_numbers, include_symbols]):
        messagebox.showerror("Error", "Please select at least one option.")
    else:
        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(tk.END, password)

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showerror("Error", "No password generated yet.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Password Length
length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Checkbox options
uppercase_var = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(root, text="Include Uppercase", variable=uppercase_var)
uppercase_checkbox.pack()

lowercase_var = tk.BooleanVar()
lowercase_checkbox = tk.Checkbutton(root, text="Include Lowercase", variable=lowercase_var)
lowercase_checkbox.pack()

numbers_var = tk.BooleanVar()
numbers_checkbox = tk.Checkbutton(root, text="Include Numbers", variable=numbers_var)
numbers_checkbox.pack()

symbols_var = tk.BooleanVar()
symbols_checkbox = tk.Checkbutton(root, text="Include Symbols", variable=symbols_var)
symbols_checkbox.pack()

# Generate Password button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Display generated password
password_entry = tk.Entry(root, show='*')
password_entry.pack()

# Copy to clipboard button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack()

root.mainloop()
