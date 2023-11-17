import tkinter as tk


class ThirdPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.entry_label = tk.Label(self, text="This is the first page")
        self.entry_label.config(font=("Helvetica", 24))
        self.entry_label.pack(pady=10)
