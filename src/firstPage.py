import tkinter as tk


class FirstPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Set the background color
        self.configure(bg="lightblue")

        self.entry_label = tk.Label(self, text="This is the 1st page")
        self.entry_label.config(font=("Helvetica", 24), bg="lightblue")
        self.entry_label.pack(pady=10)
