import tkinter as tk


class WeatherPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Set the background color
        self.configure(bg="#bbb")

        self.entry_label = tk.Label(self, text="This is weather page")
        self.entry_label.config(font=("Helvetica", 24), bg="#bbb")
        self.entry_label.pack(pady=10)
