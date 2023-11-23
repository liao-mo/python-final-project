import tkinter as tk
from tradingPage import TradingPage
from weatherPage import WeatherPage
from thirdPage import ThirdPage


class ButtonFrame(tk.Frame):
    def __init__(self, master, show_tradingPage, show_weather_page, show_third_page):
        super().__init__(master)

        # Create buttons
        self.tradingPage_button = tk.Button(
            self, text="Trading", command=show_tradingPage
        )
        self.weather_page_button = tk.Button(
            self, text="Weather", command=show_weather_page
        )
        self.third_page_button = tk.Button(
            self, text="Third Page", command=show_third_page
        )

        # Pack buttons at the top with a 5px padding
        self.tradingPage_button.pack(side=tk.LEFT, padx=5)
        self.weather_page_button.pack(side=tk.LEFT, padx=5)
        self.third_page_button.pack(side=tk.LEFT, padx=5)


class MainPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create a ButtonFrame instance
        self.button_frame = ButtonFrame(
            self, self.show_tradingPage, self.show_weather_page, self.show_third_page
        )

        # Pack the ButtonFrame at the top
        self.button_frame.pack(side=tk.TOP, pady=5)

        # Initialize the pages
        self.tradingPage = TradingPage(self)
        self.weather_page = WeatherPage(self)
        self.third_page = ThirdPage(self)

        # Show the tradingPage by default
        self.show_tradingPage()

    def show_tradingPage(self):
        self.hide_all_pages()
        self.tradingPage.pack(fill=tk.BOTH, expand=True)

    def show_weather_page(self):
        self.hide_all_pages()
        self.weather_page.pack(fill=tk.BOTH, expand=True)

    def show_third_page(self):
        self.hide_all_pages()
        self.third_page.pack(fill=tk.BOTH, expand=True)

    def hide_all_pages(self):
        self.tradingPage.pack_forget()
        self.weather_page.pack_forget()
        self.third_page.pack_forget()
