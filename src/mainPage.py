import tkinter as tk
from firstPage import FirstPage
from secondPage import SecondPage
from thirdPage import ThirdPage


class MainPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.first_page_button = tk.Button(
            self, text="Go to First Page", command=self.show_first_page)
        self.first_page_button.pack(pady=10)

        self.second_page_button = tk.Button(
            self, text="Go to Second Page", command=self.show_second_page)
        self.second_page_button.pack(pady=10)

        self.third_page_button = tk.Button(
            self, text="Go to Third Page", command=self.show_third_page)
        self.third_page_button.pack(pady=10)

        # Initialize the pages
        self.first_page = FirstPage(self)
        self.second_page = SecondPage(self)
        self.third_page = ThirdPage(self)

        # Show the first page by default
        self.show_first_page()

    def show_first_page(self):
        print("show first page")
        self.hide_all_pages()
        self.first_page.pack(fill=tk.BOTH, expand=True)

    def show_second_page(self):
        print("show second page")
        self.hide_all_pages()
        self.second_page.pack(fill=tk.BOTH, expand=True)

    def show_third_page(self):
        print("show third page")
        self.hide_all_pages()
        self.third_page.pack(fill=tk.BOTH, expand=True)

    def hide_all_pages(self):
        self.first_page.pack_forget()
        self.second_page.pack_forget()
        self.third_page.pack_forget()
