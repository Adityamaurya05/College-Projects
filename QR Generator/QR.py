import tkinter as tk
import qrcode
from PIL import Image, ImageTk
import re

def create_qr_code():
    # Gather attendee information
    attendee_name = attendee_name_entry.get()
    email_address = email_entry.get()
    twitter_account = twitter_entry.get()
    github_account = github_entry.get()
    instagram_account = instagram_entry.get()
    mobile_number = mobile_entry.get()

    # Validation
    if not attendee_name or not email_address:
        error_label.config(text="Please enter required fields.")
        return
    elif not re.match(r"[^@]+@[^@]+\.[^@]+", email_address):
        error_label.config(text="Please enter a valid email address.")
        return
    elif twitter_account and not twitter_account.startswith('@'):
        error_label.config(text="Twitter account must start with '@'.")
        return
    elif mobile_number and not re.match(r"^\d{10}$", mobile_number):
        error_label.config(text="Please enter a valid 10-digit mobile number.")
        return

    # Clear error label
    error_label.config(text="")

    # Generate QR code
    qr_data = f"Name: {attendee_name}\nEmail: {email_address}\nTwitter: {twitter_account}\nGitHub: {github_account}\nInstagram: {instagram_account}\nMobile: {mobile_number}"
    qr = qrcode.make(qr_data)
    qr = qr.resize((200, 200))

    # Display badge panel
    badge_panel.config(text=f"Name: {attendee_name}\nEmail: {email_address}\nTwitter: {twitter_account}\nGitHub: {github_account}\nInstagram: {instagram_account}\nMobile: {mobile_number}")
    qr_image = ImageTk.PhotoImage(image=qr)
    qr_panel.config(image=qr_image)
    qr_panel.image = qr_image

def clear_fields():
    # Clear input fields and badge panel
    attendee_name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    twitter_entry.delete(0, tk.END)
    github_entry.delete(0, tk.END)
    instagram_entry.delete(0, tk.END)
    mobile_entry.delete(0, tk.END)
    badge_panel.config(text="")
    qr_panel.config(image="")
    error_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Attendee Badge Generator")

# Input fields
attendee_name_label = tk.Label(root, text="Attendee Name:")
attendee_name_label.grid(row=0, column=0)
attendee_name_entry = tk.Entry(root)
attendee_name_entry.grid(row=0, column=1)

email_label = tk.Label(root, text="Email Address:")
email_label.grid(row=1, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1)

twitter_label = tk.Label(root, text="Twitter Account:")
twitter_label.grid(row=2, column=0)
twitter_entry = tk.Entry(root)
twitter_entry.grid(row=2, column=1)

github_label = tk.Label(root, text="GitHub Account:")
github_label.grid(row=3, column=0)
github_entry = tk.Entry(root)
github_entry.grid(row=3, column=1)

instagram_label = tk.Label(root, text="Instagram Account:")
instagram_label.grid(row=4, column=0)
instagram_entry = tk.Entry(root)
instagram_entry.grid(row=4, column=1)

mobile_label = tk.Label(root, text="Mobile Number:")
mobile_label.grid(row=5, column=0)
mobile_entry = tk.Entry(root)
mobile_entry.grid(row=5, column=1)

# Error label
error_label = tk.Label(root, fg="red")
error_label.grid(row=6, columnspan=2)

# Buttons
create_button = tk.Button(root, text="Create", command=create_qr_code)
create_button.grid(row=7, column=0)

cancel_button = tk.Button(root, text="Cancel", command=clear_fields)
cancel_button.grid(row=7, column=1)

# Badge panel
badge_panel = tk.Label(root, text="")
badge_panel.grid(row=8, columnspan=2)

# QR Code panel
qr_panel = tk.Label(root)
qr_panel.grid(row=9, columnspan=2)

root.mainloop()
