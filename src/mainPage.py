import tkinter as tk
from tradingPage import TradingPage
from weatherPage import WeatherPage
from nbaPage import NBAPage


class ButtonFrame(tk.Frame):
    def __init__(self, master, show_tradingPage, show_weather_page, show_nba_page):
        super().__init__(master)

        # Create buttons
        self.tradingPage_button = tk.Button(
            self, text="Trading", command=show_tradingPage
        )
        self.weather_page_button = tk.Button(
            self, text="Weather", command=show_weather_page
        )
        self.nba_page_button = tk.Button(self, text="NBA", command=show_nba_page)

        # Pack buttons at the top with a 5px padding
        self.tradingPage_button.pack(side=tk.LEFT, padx=5)
        self.weather_page_button.pack(side=tk.LEFT, padx=5)
        self.nba_page_button.pack(side=tk.LEFT, padx=5)


class MainPage(tk.Frame):
    def __init__(self, master, line_api_key):
        super().__init__(master)

        # Create a ButtonFrame instance
        self.button_frame = ButtonFrame(
            self, self.show_tradingPage, self.show_weather_page, self.show_nba_page
        )

        # Pack the ButtonFrame at the top
        self.button_frame.pack(side=tk.TOP, pady=5)

        # Initialize the pages
        self.tradingPage = TradingPage(self, line_api_key)
        self.weather_page = WeatherPage(self, line_api_key)
        self.nba_page = NBAPage(self, line_api_key)

        # Show the tradingPage by default
        self.show_tradingPage()

    def show_tradingPage(self):
        self.hide_all_pages()
        self.tradingPage.pack(fill=tk.BOTH, expand=True)

    def show_weather_page(self):
        self.hide_all_pages()
        self.weather_page.pack(fill=tk.BOTH, expand=True)

    def show_nba_page(self):
        self.hide_all_pages()
        self.nba_page.pack(fill=tk.BOTH, expand=True)

    def hide_all_pages(self):
        self.tradingPage.pack_forget()
        self.weather_page.pack_forget()
        self.nba_page.pack_forget()
