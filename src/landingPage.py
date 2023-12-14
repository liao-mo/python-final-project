import tkinter as tk


class LandingPage(tk.Frame):
    def __init__(self, master):
        """
        Initialize the LandingPage.

        Args:
            master: Parent tkinter window or frame.
        """
        super().__init__(master)

        # Label for API key entry
        self.entry_label = tk.Label(self, text="Enter API Key:")
        self.entry_label.config(font=("Helvetica", 24))
        self.entry_label.pack(pady=10)

        # Entry widget for API key input
        self.temp_api = tk.StringVar(
            value="L5ndN5HrN07x8RQkJ03znyCOzGfLIQ3FSFkZdT3SoWo"
        )
        self.entry = tk.Entry(self, width="100", textvariable=self.temp_api)
        self.entry.pack(padx=10, pady=10)

        # Continue button
        self.continue_button = tk.Button(self, text="Continue")
        self.continue_button.config(font=("Helvetica", 24))
        self.continue_button.pack(pady=20)
