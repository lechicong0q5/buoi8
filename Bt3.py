import customtkinter as ctk
from tkinter import Canvas, Scrollbar


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


for i in range(1000):
    button = ctk.CTkButton(inner_frame, text=f"Button {i+1}")
    button.pack(pady=2)


inner_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))


app.mainloop()
