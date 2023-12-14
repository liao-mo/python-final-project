import tkinter as tk
from landingPage import LandingPage
from mainPage import MainPage
import requests

# 1v1 api-key: L5ndN5HrN07x8RQkJ03znyCOzGfLIQ3FSFkZdT3SoWo
# group api-key: aXeGGuxXR4KFNZlMXg0yfvIwD2ledWRD3mQI0L2Sume


class MainApp(tk.Tk):
    def __init__(self):
        """
        Constructor for the MainApp class.

        Initializes the Tkinter application with the LandingPage as the initial page.
        """
        super().__init__()
        self.title("Multi-Page Tkinter App")
        self.geometry("800x600")
        self.show_first_page()

    def show_first_page(self):
        """
        Show the LandingPage.

        Packs and displays the LandingPage, configuring the continue button to check the API key.
        """
        self.first_page = LandingPage(self)
        self.first_page.pack(fill=tk.BOTH, expand=True)
        self.first_page.continue_button.config(command=self.check_api_key)

    def check_api_key(self):
        """
        Check the validity of the entered API key.

        Retrieves the API key from the LandingPage entry, performs an availability check, and proceeds to
        the weather page if the key is valid.
        """
        # Retrieve API key from the first page
        self.api_key = self.first_page.entry.get()
        print("Entered API Key:", self.api_key)

        # Perform API key availability check (replace with your actual API check logic)
        try:
            api_endpoint = f"https://notify-api.line.me/api/notify?message=Activating with python app..."
            headers = {"Authorization": f"Bearer {self.api_key}"}
            # Make a POST request
            response = requests.post(api_endpoint, headers=headers)

            # Check the response
            if response.status_code == 200:
                print("API Key is valid. Proceeding to the weather page.")
                self.show_main_page()
            else:
                print("Invalid API Key.")
        except Exception as e:
            print(f"Error: {e}")

    def show_main_page(self):
        """
        Show the MainPage.

        Forgets the first page and creates/shows the MainPage.
        """
        # Remove the first page
        self.first_page.pack_forget()

        # Create and show the main page
        self.main_page = MainPage(self, self.api_key)
        self.main_page.pack(fill=tk.BOTH, expand=True)


if __name__ == "__main__":
    # Run the Tkinter application
    app = MainApp()
    app.mainloop()
