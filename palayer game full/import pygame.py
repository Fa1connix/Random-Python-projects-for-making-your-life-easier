import customtkinter
from tkinter import *
import tkinter as tk
 
 
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
 
 
root=customtkinter.CTk()
root.geometry('500x300')
 
def login():
    print("My passcode is meme")
   
 
frame= customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)
 
 
label=customtkinter.CTkLabel(master=frame, text="enter user", text_font=("Roboto", 24))
label.pack(pady=12, padx=10)
 
usr=customtkinter.CTkEntry(master=frame, placeholder_text="Username")
usr.pack(pady=12, padx=10)
 
psw=customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
psw.pack(pady=12, padx=10)
 
button= customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx =10)
 
checkbox=customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)
 
#usrinp=tk.
#
# usrinp.pack(pady=12, padx=10)
 
 
root.mainloop()
