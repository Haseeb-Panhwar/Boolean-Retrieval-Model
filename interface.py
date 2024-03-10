import tkinter as tk
import customtkinter as ct

ct.set_appearance_mode("System")
ct.set_default_color_theme("blue")
larger_font = ('Arial', 18)
app=ct.CTk()
app.geometry("720x480")
app.title("Boolean Retrieval Search")

title = ct.CTkLabel(app,text="Enter Boolean Query",font=larger_font)
title.pack(padx=10,pady=10)

query = ct.CTkEntry(app,width=400,height=40)
query.pack()

app.mainloop()