# Program to encrypt and decrypt text using ceasor cipher algorithm.
import tkinter as tk
from tkinter.ttk import *

# Main program to encrypt and decrypt text using ceasor cipher algorithm



# GUI implementation
root = tk.Tk()
root.title("CaesarLock")
root.geometry("1200x580")
root.resizable(False, False)

#icon
icon = tk.PhotoImage(file = "./assets/icon.png")
root.iconphoto(False, icon)

menu = tk.Menu(root)
root.config(menu=menu)

root.mainloop()