import tkinter as tk
from tkinter import messagebox
import numpy as np
from PIL import Image, ImageTk

# Task 1: Encryption Algorithm (Caesar cipher)
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_text += char
    return encrypted_text

# Task 2: User Identity Verification (Placeholder)
def verify_typing_pattern(new_typing_pattern):
    # Placeholder: Randomly assign verification result
    verification_result = np.random.choice(["Verified", "Not Verified"])  # Simulating verification
    return verification_result

# GUI
def encrypt_and_verify():
    message = input_text.get("1.0", "end-1c")
    if not message:
        messagebox.showerror("Error", "Please enter a message")
        return
    
    shift = 3
    encrypted = caesar_encrypt(message, shift)
    
    typing_pattern_input = typing_pattern_entry.get().strip()
    if not typing_pattern_input:  # Check if typing pattern is empty
        messagebox.showerror("Error", "Please enter typing speed intervals")
        return
    
    typing_pattern_list = typing_pattern_input.split()
    
    try:
        typing_pattern = [int(interval) for interval in typing_pattern_list]
    except ValueError:
        messagebox.showerror("Error", "Invalid typing pattern format")
        return
    
    verification_result = verify_typing_pattern(typing_pattern)
    
    output_text.config(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("1.0", f"User Input: {message}\nEncrypted: {encrypted}\nVerification Result: {verification_result}")
    output_text.config(state="disabled")

# Create the main GUI window
root = tk.Tk()
root.title("Message Encryption and Verification")
root.geometry("800x600")  # Set window dimensions

# Load the background image
background_image = Image.open("C:\\Users\\HP\\OneDrive\\Desktop\\coding\\python\\background.jpg")  # Replace with your image path
background_photo = ImageTk.PhotoImage(background_image)

# Create a label to display the background image
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# Input Text Area
input_label = tk.Label(root, text="Enter a message:", fg="green")
input_label.pack()

input_text = tk.Text(root, height=3, width=40, bg="black", fg="blue")
input_text.pack()

# Already Written Messages
default_message = "Enter your message here..."
input_text.insert("1.0", default_message)
input_text.tag_add("green", "1.0", "end")
input_text.tag_config("green", foreground="green")

def on_click(event):
    if input_text.get("1.0", "end-1c") == default_message:
        input_text.delete("1.0", "end")
        input_text.configure(fg="blue")  # Change text color to blue

input_text.bind("<Button-1>", on_click)

# Typing Pattern Entry
typing_pattern_label = tk.Label(root, text="Enter typing pattern (space-separated intervals):", fg="green")
typing_pattern_label.pack()

typing_pattern_entry = tk.Entry(root, bg="black", fg="green")
typing_pattern_entry.pack()

# Encrypt and Verify Button
encrypt_verify_button = tk.Button(root, text="Encrypt and Verify", command=encrypt_and_verify, bg="black", fg="green")
encrypt_verify_button.pack()

# Output Text Area
output_label = tk.Label(root, text="Output:", fg="green")
output_label.pack()

output_text = tk.Text(root, height=5, width=40, bg="black", fg="blue")
output_text.pack()

# Center align the Output Text Area
output_text.tag_configure("center", justify="center")
output_text.insert("1.0", "Output text here...")
output_text.tag_add("center", "1.0", "end")
output_text.configure(state="disabled")

# Start the GUI main loop
root.mainloop()
