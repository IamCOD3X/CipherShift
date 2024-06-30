import tkinter as tk
from tkinter.ttk import *
import pyfiglet

# Main program to encrypt and decrypt text using Caesar Cipher algorithm
def insert_console_output(text):
    console_output.insert(tk.END, text + "\n")
    console_output.see(tk.END)  # Scroll to the end

def encrypt():
    shift = int(encrypt_shift_var.get())
    plaintext = input_text.get("1.0", tk.END).strip()
    ciphertext = ''
    
    for char in plaintext:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char) - ord('A' if char.isupper() else 'a') + shift_amount) % 26) + ord('A' if char.isupper() else 'a'))
            ciphertext += new_char
        else:
            ciphertext += char
            
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, ciphertext)
    insert_console_output('')
    insert_console_output(f'Your plain text "{plaintext}" has been Encrypted.')
    insert_console_output(f"Encrypted Text is: {ciphertext}")
    insert_console_output(f'Using Shift: {shift}')

def decrypt():
    shift = int(decrypt_shift_var.get())
    ciphertext = output_text.get("1.0", tk.END).strip()
    plaintext = ''
    
    for char in ciphertext:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char) - ord('A' if char.isupper() else 'a') - shift_amount) % 26) + ord('A' if char.isupper() else 'a'))
            plaintext += new_char
        else:
            plaintext += char
            
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, plaintext)
    insert_console_output('')
    insert_console_output(f'Your cipher text "{ciphertext}" has been decrypted.')
    insert_console_output(f"Decrypted Text is: {plaintext}")
    insert_console_output(f'Using Shift: {shift}')

# GUI implementation
root = tk.Tk()
root.title("CaesarLock")
root.geometry("1200x700")  # Adjusted height to accommodate all elements
root.resizable(False, False)

# Icon
icon = tk.PhotoImage(file="./assets/icon.png")
root.iconphoto(False, icon)

# Console Output Text Widget
console_output = tk.Text(root, height=12, width=80)
console_output.pack(pady=10)

ascii_text = pyfiglet.figlet_format("CaesarLock", font="small", width=60)
insert_console_output(ascii_text)

ascii_text = pyfiglet.figlet_format("By IamCOD3X", font="small", width=60)
insert_console_output(ascii_text)

# Creating a canvas to draw the dividing line
canvas = tk.Canvas(root, width=1200, height=550)
canvas.pack()
canvas.create_line(600, 0, 600, 700, fill="red")

# Creating widgets for encryption (left side)
input_label = tk.Label(root, text="Encrypt Text:")
input_label.place(x=50, y=220)
input_text = tk.Text(root, height=10, width=50)
input_text.place(x=50, y=260)

encrypt_shift_label = tk.Label(root, text="Encrypt Shift:")
encrypt_shift_label.place(x=50, y=440)
encrypt_shift_var = tk.StringVar()
encrypt_shift_combo = Combobox(root, textvariable=encrypt_shift_var, values=list(range(26)))
encrypt_shift_combo.place(x=50, y=470)
encrypt_shift_combo.current(1)  # Default to 1 shift

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.place(x=50, y=500)

# Creating widgets for decryption (right side)
output_label = tk.Label(root, text="Decrypt Text:")
output_label.place(x=650, y=220)
output_text = tk.Text(root, height=10, width=50)
output_text.place(x=650, y=260)

decrypt_shift_label = tk.Label(root, text="Decrypt Shift:")
decrypt_shift_label.place(x=650, y=440)
decrypt_shift_var = tk.StringVar()
decrypt_shift_combo = Combobox(root, textvariable=decrypt_shift_var, values=list(range(26)))
decrypt_shift_combo.place(x=650, y=470)
decrypt_shift_combo.current(1)  # Default to 1 shift

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
decrypt_button.place(x=650, y=500)

# Starting the GUI event loop
root.mainloop()
