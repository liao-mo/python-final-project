import tkinter as tk
from trading import *
from lineNotify import *
import ast
import uuid


class TradingPage(tk.Frame):
    def __init__(self, master, line_api_key):
        """
        Initialize the TradingPage.

        Args:
            master (tk.Tk): The master Tkinter window.
            line_api_key (str): Line Notify API key.
        """
        super().__init__(master)

        self.lineUser = LineNotify(line_api_key)

        self.tasks = []

        # Set the background color
        self.configure(bg="#fff5f5")

        # 1st row
        self.symbol_label = tk.Label(self, text="Market symbol")
        self.symbol_label.config(font=("Helvetica", 12), bg="#fff5f5")
        self.symbol_label.grid(column=0, row=0, pady=10, padx=5)

        self.symbols = epics.keys()
        self.selected_symbol = tk.StringVar()
        self.selected_symbol.set("BTCUSD")

        self.menu_symbols = tk.OptionMenu(self, self.selected_symbol, *self.symbols)
        self.menu_symbols.grid(column=1, row=0, sticky=tk.W, pady=10, padx=5)

        # 2nd row
        self.btn_sendSeleted = tk.Button(
            self, text="Send current price", command=self.sendSeletedPrice
        )
        self.btn_sendSeleted.config(font=("Helvetica", 12), bg="#fff5f5")
        self.btn_sendSeleted.grid(column=0, row=1, sticky=tk.W + tk.E, pady=10, padx=5)

        self.btn_sendAll = tk.Button(
            self, text="Send all prices", command=self.sendAllPrice
        )
        self.btn_sendAll.config(font=("Helvetica", 12), bg="#fff5f5")
        self.btn_sendAll.grid(column=1, row=1, sticky=tk.W, pady=10, padx=5)

        # 3rd row
        self.label_period = tk.Label(self, text="Send notification Every")
        self.label_period.config(font=("Helvetica", 12), bg="#fff5f5")
        self.label_period.grid(column=0, row=3, sticky=tk.W + tk.E, pady=10, padx=5)

        self.spinbox_period = tk.Spinbox(self, from_=1, to=60, width=10)
        self.spinbox_period.config(font=("Helvetica", 20), bg="#fff5f5")
        self.spinbox_period.grid(column=1, row=3, sticky=tk.W, pady=10, padx=5)

        self.time_units = ["seconds", "minutes", "hours"]
        self.selected_time_unit = tk.StringVar()
        self.selected_time_unit.set("seconds")

        self.menu_time_units = tk.OptionMenu(
            self, self.selected_time_unit, *self.time_units
        )
        self.menu_time_units.grid(column=2, row=3, sticky=tk.W, pady=10, padx=5)

        self.btn_period = tk.Button(
            self,
            text="Submit",
            command=lambda: self.add_new_task(
                "periodic",
                self.calculatePeriod(),
                {"symbol": self.selected_symbol.get()},
            ),
        )
        self.btn_period.config(font=("Helvetica", 12), bg="#fff5f5")
        self.btn_period.grid(column=3, row=3, sticky=tk.W + tk.E, pady=10, padx=5)

        # 4th row
        self.label_comparison = tk.Label(self, text="Send notification when the price")
        self.label_comparison.config(font=("Helvetica", 12), bg="#fff5f5")
        self.label_comparison.grid(column=0, row=4, sticky=tk.W + tk.E, pady=10, padx=5)

        self.comp_operators = ["<", ">", "increase", "decrease"]
        self.selected_comp_operators = tk.StringVar()
        self.selected_comp_operators.set("<")
        self.menu_comparison = tk.OptionMenu(
            self, self.selected_comp_operators, *self.comp_operators
        )
        self.menu_comparison.grid(column=1, row=4, sticky=tk.W + tk.E, pady=10, padx=10)

        self.comparison_number = tk.DoubleVar()
        self.entry_comparison = tk.Entry(self, textvariable=self.comparison_number)
        self.entry_comparison.config(font=("Helvetica", 12), bg="#fff5f5")
        self.entry_comparison.grid(column=2, row=4, sticky=tk.W + tk.E, pady=10, padx=5)

        self.btn_comparison = tk.Button(
            self,
            text="Submit",
            command=lambda: self.add_new_task(
                "comparison",
                10000,
                {
                    "symbol": self.selected_symbol.get(),
                    "operator": self.selected_comp_operators.get(),
                    "value": self.comparison_number.get(),
                },
            ),
        )
        self.btn_comparison.config(font=("Helvetica", 12), bg="#fff5f5")
        self.btn_comparison.grid(column=3, row=4, sticky=tk.W + tk.E, pady=10, padx=5)

        # tasks listbox
        self.tasks_string = tk.StringVar()
        self.listbox_tasks = tk.Listbox(self, listvariable=self.tasks_string)
        self.listbox_tasks.grid(
            column=0, row=5, columnspan=3, sticky=tk.W + tk.E, pady=10, padx=5
        )

        self.btn_delete_task = tk.Button(
            self,
            text="Delete",
            command=lambda: self.deleteTask(self.getCurrentSeletedTaskIndex()),
        )
        self.btn_delete_task.config(font=("Helvetica", 12), bg="#fff5f5")
        self.btn_delete_task.grid(column=3, row=5, sticky=tk.W + tk.E, pady=10, padx=5)

    def sendSeletedPrice(self):
        """
        Send a Line Notify message with the current price of the selected symbol.
        """
        symbol = self.selected_symbol.get()
        avgPrice = self.getPrice(symbol)
        message = f"{symbol}\nCurrent price: {avgPrice:.6g}"
        self.lineUser.send_message(message)

    def sendAllPrice(self):
        """
        Send a Line Notify message with the current prices of all symbols.
        """
        symbols = epics.keys()
        message = ""
        for symbol in symbols:
            avgPrice = self.getPrice(symbol)
            message += f"{symbol}\nCurrent price: {avgPrice:.6g}\n\n"
        self.lineUser.send_message(message)

    def add_new_task(self, taskType, new_interval, params):
        """
        Add a new task to the scheduled tasks list.

        Args:
            taskType (str): Type of the task ('periodic' or 'comparison').
            new_interval (int): Interval for periodic tasks.
            params (dict): Parameters for the task.

        Returns:
            None
        """

        lastPrice = self.getPrice(params["symbol"])
        params["lastPrice"] = lastPrice
        new_task = {
            "_id": str(uuid.uuid4()),
            "type": taskType,
            "interval": new_interval,
            "params": params,
        }
        self.tasks.append(new_task)

        # append task description to the string_list
        temp_str_list = []
        if self.tasks_string.get() != "":
            temp_str_list = ast.literal_eval(self.tasks_string.get())
        temp_str_list = list(temp_str_list)

        if taskType == "periodic":
            temp_str_list.append(
                f'{params["symbol"]} notify interval: {new_interval / 1000.0}s'
            )
        elif taskType == "comparison":
            temp_str_list.append(
                f'{params["symbol"]} notify when the price {params["operator"]} {params["value"]}'
            )
        self.tasks_string.set(temp_str_list)

        self.schedule_task(new_task)

    def schedule_task(self, task):
        """
        Schedule a task to be executed after a specified interval.

        Args:
            task (dict): Task dictionary containing task details.

        Returns:
            None
        """
        # Check if the task with a specific UUID is in the list
        searched_uuid = task["_id"]
        found_task = next((t for t in self.tasks if t["_id"] == searched_uuid), None)
        if not found_task:
            return

        # Call the task function with parameters
        if task["type"] == "periodic":
            # Unpack parameters using **kwargs
            self.periodicTask(task["params"]["symbol"])
        elif task["type"] == "comparison":
            symbol = task["params"]["symbol"]
            self.comparisonTask(**task["params"], uid=task["_id"])

        # call the schedule_task function again after the interval
        self.after(task["interval"], lambda: self.schedule_task(task))

    def periodicTask(self, symbol):
        """
        Perform actions for a periodic task.

        Args:
            symbol (str): Trading symbol.

        Returns:
            None
        """
        avgPrice = self.getPrice(symbol)
        message = f"{symbol}\nCurrent price: {avgPrice:.6g}"
        print(f"Sending {message}")
        self.lineUser.send_message(message)

    def comparisonTask(self, lastPrice, symbol, operator, value, uid):
        """
        Perform actions for a comparison task.

        Args:
            lastPrice (float): Last known price.
            symbol (str): Trading symbol.
            operator (str): Comparison operator ('<', '>', 'increase', 'decrease').
            value (float): Comparison value.
            uid (str): Unique identifier for the task.

        Returns:
            None
        """
        current_price = self.getPrice(symbol)
        if operator == "<":
            if current_price < value:
                message = f"{symbol} is now lower than {value}!"
                self.lineUser.send_message(message)

                # delete the task after notification
                index = self.findIndexByUid(uid)
                self.deleteTask(index)
        elif operator == ">":
            if current_price > value:
                message = f"{symbol} is now higher than {value}!"
                self.lineUser.send_message(message)

                # delete the task after notification
                index = self.findIndexByUid(uid)
                self.deleteTask(index)
        elif operator == "increase":
            if current_price - lastPrice > value:
                message = f"{symbol} has increased {value}!"
                self.lineUser.send_message(message)

                # delete the task after notification
                index = self.findIndexByUid(uid)
                self.deleteTask(index)
        elif operator == "decrease":
            if lastPrice - current_price > value:
                message = f"{symbol} has decreased {value}!"
                self.lineUser.send_message(message)

                # delete the task after notification
                index = self.findIndexByUid(uid)
                self.deleteTask(index)

    def calculatePeriod(self):
        """
        Calculate the task interval based on user input.

        Returns:
            int: Task interval in milliseconds.
        """
        time = 1000
        if self.selected_time_unit.get() == "seconds":
            time = int(self.spinbox_period.get()) * 1000
        elif self.selected_time_unit.get() == "minutes":
            time = int(self.spinbox_period.get()) * 1000 * 60
        elif self.selected_time_unit.get() == "hours":
            time = int(self.spinbox_period.get()) * 1000 * 60 * 60
        return time

    def getCurrentSeletedTaskIndex(self):
        """
        Get the index of the currently selected task in the listbox.

        Returns:
            int: Index of the selected task.
        """
        try:
            (i,) = self.listbox_tasks.curselection()
            return i
        except ValueError:
            # Handle the case where there are not enough values to unpack
            print("No item selected")
            return -1

    def deleteTask(self, index_to_delete):
        """
        Delete a task from the scheduled tasks list.

        Args:
            index_to_delete (int): Index of the task to delete.

        Returns:
            None
        """
        if index_to_delete < 0:
            return

        del self.tasks[index_to_delete]
        temp_str_list = []
        if self.tasks_string.get() != "":
            temp_str_list = ast.literal_eval(self.tasks_string.get())
        temp_str_list = list(temp_str_list)
        del temp_str_list[index_to_delete]
        self.tasks_string.set(temp_str_list)

    def getPrice(self, symbol):
        """
        Get the current average price for a given symbol.

        Args:
            symbol (str): Trading symbol.

        Returns:
            float: Average price.
        """
        market_info = get_market_info(epics.get(symbol))
        avgPrice = 0
        try:
            avgPrice = (float(market_info["bid"]) + float(market_info["offer"])) / 2.0
        except Exception as e:
            return -1
        return avgPrice

    def findIndexByUid(self, uid):
        """
        Find the index of a task in the scheduled tasks list by UID.

        Args:
            uid (str): Unique identifier.

        Returns:
            int or None: Index of the task if found, None otherwise.
        """
        for index, d in enumerate(self.tasks):
            if d["_id"] == uid:
                return index
        return None  # Return None if 'uid_to_find' is not found
