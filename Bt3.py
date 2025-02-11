import customtkinter as ctk
from tkinter import Canvas, Scrollbar
import threading
import time


app = ctk.CTk()
app.title("Tên Của Bạn")
app.geometry("600x500")
app.resizable(False, False)


frame = ctk.CTkFrame(app)
frame.pack(fill="both", expand=True)


canvas = Canvas(frame)
canvas.pack(side="left", fill="both", expand=True)


scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)


inner_frame = ctk.CTkFrame(canvas)
canvas.create_window((0, 0), window=inner_frame, anchor="nw")


buttons = []


num_buttons = 1000
batch_size = 50
interval = 5


def create_buttons(start, end):
    for i in range(start, end):
        button = ctk.CTkButton(inner_frame, text=f"Button {i+1}")
        button.pack(pady=2)
        buttons.append(button)
    

    inner_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    

    if end < num_buttons:
        app.after(interval * 1000, create_buttons, end, min(end + batch_size, num_buttons))

create_buttons(0, batch_size)


app.mainloop()