import customtkinter as ctk
from tkinter import Canvas, Scrollbar
from PIL import Image, ImageTk
import os


app = ctk.CTk()
app.title("Gallery iPhone")
app.geometry("600x600")
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

image_files = ["./hinhanh/1.jfif", "./hinhanh/2.jfif", "./hinhanh/3.jfif", "./hinhanh/4.jfif"]


rows, cols = 10, 4
for row in range(rows):
    for col in range(cols):
        img_path = image_files[col % len(image_files)] 

        if os.path.exists(img_path): 
            img = Image.open(img_path)
            img = img.resize((100, 100)) 
            img = ImageTk.PhotoImage(img)

            card = ctk.CTkLabel(inner_frame, image=img, text=f"Ảnh {col+1}")
            card.image = img
            card.grid(row=row, column=col, padx=10, pady=10)
        else:
            print(f"❌ Không tìm thấy ảnh: {img_path}")


inner_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))


app.mainloop()
