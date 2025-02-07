import customtkinter as ctk


app = ctk.CTk()
app.title("Tên Của Bạn")
app.geometry("600x600")
app.resizable(False, False)


frame1 = ctk.CTkFrame(app, fg_color="yellow")
frame2 = ctk.CTkFrame(app, fg_color="red")
frame3 = ctk.CTkFrame(app, fg_color="gray")
frame4 = ctk.CTkFrame(app, fg_color="blue")


frame1.grid(row=0, column=0, sticky="nsew")
frame2.grid(row=0, column=1, sticky="nsew")
frame3.grid(row=1, column=0, sticky="nsew")
frame4.grid(row=1, column=1, sticky="nsew")


app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)


app.mainloop()
