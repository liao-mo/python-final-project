import tkinter as tk


class ThirdPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Set the background color
        self.configure(bg="#81c994")

        self.entry_label = tk.Label(self, text="This is the 3rd page")
        self.entry_label.config(font=("Helvetica", 24), bg="#81c994")
        self.entry_label.pack(pady=10)
