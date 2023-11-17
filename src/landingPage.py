import tkinter as tk


class LandingPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.entry_label = tk.Label(self, text="Enter API Key:")
        self.entry_label.config(font=("Helvetica", 24))
        self.entry_label.pack(pady=10)

        self.entry = tk.Entry(self, width="100")
        self.entry.pack(padx=10, pady=10)

        self.continue_button = tk.Button(self, text="Continue")
        self.continue_button.config(font=("Helvetica", 24))
        self.continue_button.pack(pady=20)
