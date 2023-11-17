import tkinter as tk
from firstPage import FirstPage
from secondPage import SecondPage
from thirdPage import ThirdPage

class ButtonFrame(tk.Frame):
    def __init__(self, master, show_first_page, show_second_page, show_third_page):
        super().__init__(master)


        # Create buttons
        self.first_page_button = tk.Button(self, text="First Page", command=show_first_page)
        self.second_page_button = tk.Button(self, text="Second Page", command=show_second_page)
        self.third_page_button = tk.Button(self, text="Third Page", command=show_third_page)

        # Pack buttons at the top with a 5px padding
        self.first_page_button.pack(side=tk.LEFT, padx=5)
        self.second_page_button.pack(side=tk.LEFT, padx=5)
        self.third_page_button.pack(side=tk.LEFT, padx=5)

class MainPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create a ButtonFrame instance
        self.button_frame = ButtonFrame(
            self,
            self.show_first_page,
            self.show_second_page,
            self.show_third_page
        )

        # Pack the ButtonFrame at the top
        self.button_frame.pack(side=tk.TOP, pady=5)

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
