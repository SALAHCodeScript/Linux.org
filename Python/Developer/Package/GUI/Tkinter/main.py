import tkinter as tk

app = tk.Tk()
app.title("Custom Application")
app.geometry("1024x600")
app.config(background="#000")

label = tk.Label(text="Some Text", fg="#000", bg="#fff", font=("0xProto Nerd Font Mono", 20, "bold"), bd=5, relief="solid", padx=10, pady=10)
label.pack()

app.mainloop()
