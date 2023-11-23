import tkinter as tk
from landingPage import LandingPage
from mainPage import MainPage
import requests

# 1v1 api-key: L5ndN5HrN07x8RQkJ03znyCOzGfLIQ3FSFkZdT3SoWo
# group api-key: aXeGGuxXR4KFNZlMXg0yfvIwD2ledWRD3mQI0L2Sume
# IG api-key: 44ac979fa1a93690779469a62b5378c051993017
# IG username: hanknine-demo
# IG password: aA12345678


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi-Page Tkinter App")
        self.geometry("800x600")

        # build code
        self.show_first_page()

        # dev code
        # self.show_first_page()
        # self.show_second_page()

    def show_first_page(self):
        self.first_page = LandingPage(self)
        self.first_page.pack(fill=tk.BOTH, expand=True)
        self.first_page.continue_button.config(command=self.check_api_key)

    def check_api_key(self):
        # Retrieve API key from the first page
        api_key = self.first_page.entry.get()

        print("Entered API Key:", api_key)

        # Perform API key availability check (replace with your actual API check logic)
        try:
            api_endpoint = f"https://notify-api.line.me/api/notify?message=Activating with python app..."
            headers = {"Authorization": f"Bearer {api_key}"}
            # Make a POST request
            response = requests.post(api_endpoint, headers=headers)

            # Check the response
            if response.status_code == 200:
                print("API Key is valid. Proceeding to the weather page.")
                self.show_weather_page()
            else:
                print(
                    "API Key is not valid. Display an error message or take appropriate action."
                )
        except Exception as e:
            print(f"Error: {e}")

    def show_weather_page(self):
        # Remove the first page
        self.first_page.pack_forget()

        # Create and show the second page
        self.weather_page = MainPage(self)
        self.weather_page.pack(fill=tk.BOTH, expand=True)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
