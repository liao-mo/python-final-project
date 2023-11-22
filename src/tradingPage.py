import tkinter as tk
from trading import *
from utility import *
from lineNotify import *
import ast
import uuid


class TradingPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.lineUser = LineNotify()

        self.tasks = []

        # Set the background color
        self.configure(bg="#fff5f5")

        # 1st row
        self.symbol_label = tk.Label(self, text="Market symbol")
        self.symbol_label.config(font=("Helvetica", 12), bg="#fff5f5")
        self.symbol_label.grid(column=0, row=0, sticky=tk.W + tk.E, pady=10, padx=5)

        self.symbols = epics.keys()
        self.selected_symbol = tk.StringVar()
        self.selected_symbol.set("BTCUSD")

        self.menu_symbols = tk.OptionMenu(self, self.selected_symbol, *self.symbols)
        self.menu_symbols.grid(column=1, row=0, sticky=tk.W + tk.E, pady=10, padx=5)

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
        self.btn_sendAll.grid(column=1, row=1, sticky=tk.W + tk.E, pady=10, padx=5)

        # 3rd row
        self.label_period = tk.Label(self, text="Send notification Every")
        self.label_period.config(font=("Helvetica", 12), bg="#fff5f5")
        self.label_period.grid(column=0, row=3, sticky=tk.W + tk.E, pady=10, padx=5)

        self.spinbox_period = tk.Spinbox(self, from_=1, to=60)
        self.spinbox_period.config(font=("Helvetica", 20), bg="#fff5f5")
        self.spinbox_period.grid(column=1, row=3, sticky=tk.W + tk.E, pady=10, padx=5)

        self.time_units = ["seconds", "minutes", "hours"]
        self.selected_time_unit = tk.StringVar()
        self.selected_time_unit.set("seconds")

        self.menu_time_units = tk.OptionMenu(
            self, self.selected_time_unit, *self.time_units
        )
        self.menu_time_units.grid(column=2, row=3, sticky=tk.W + tk.E, pady=10, padx=5)

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

        # tasks listbox
        self.tasks_string = tk.StringVar()
        self.listbox_tasks = tk.Listbox(self, listvariable=self.tasks_string)
        self.listbox_tasks.grid(
            column=0, row=4, columnspan=3, sticky=tk.W + tk.E, pady=10, padx=5
        )

        self.btn_delete_task = tk.Button(self, text="Delete", command=self.deleteTask)
        self.btn_delete_task.config(font=("Helvetica", 12), bg="#fff5f5")
        self.btn_delete_task.grid(column=3, row=4, sticky=tk.W + tk.E, pady=10, padx=5)

    def sendSeletedPrice(self):
        symbol = self.selected_symbol.get()
        market_info = get_market_info(epics.get(symbol))
        avgPrice = (float(market_info["bid"]) + float(market_info["offer"])) / 2.0
        message = f"{symbol}\nCurrent price: {avgPrice:.6g}"
        self.lineUser.send_message(message)

    def sendAllPrice(self):
        symbols = epics.keys()
        message = ""
        for symbol in symbols:
            market_info = get_market_info(epics.get(symbol))
            avgPrice = (float(market_info["bid"]) + float(market_info["offer"])) / 2.0
            message += f"{symbol}\nCurrent price: {avgPrice:.6g}\n\n"
        self.lineUser.send_message(message)

    def add_new_task(self, taskType, new_interval, params):
        # Create a new task dictionary and schedule it
        new_task = {"_id": str(uuid.uuid4()), "type": taskType, "interval": new_interval, "params": params}
        self.tasks.append(new_task)
        
        #append task description to the string_list
        temp_str_list = []
        if(self.tasks_string.get() != ""):
            temp_str_list = ast.literal_eval(self.tasks_string.get())
        temp_str_list = list(temp_str_list)
        if taskType == "periodic":
            temp_str_list.append(f"{params["symbol"]} type: {taskType} interval: {new_interval / 1000.0}s")
        elif taskType == "comparison":
            pass
        self.tasks_string.set(temp_str_list)
        
        self.schedule_task(new_task)

    def schedule_task(self, task):
        # Check if the task with a specific UUID is in the list
        searched_uuid = task["_id"]
        found_task = next((t for t in self.tasks if t["_id"] == searched_uuid), None)
        
        if not found_task:
            return
        
        if task["type"] == "periodic":
            # Call the task function with parameters and schedule it again
            self.periodicTask(**task["params"])  # Unpack parameters using **kwargs
            self.after(task["interval"], lambda: self.schedule_task(task))
        elif task["type"] == "comparison":
            pass

    def periodicTask(self, symbol):
        print(f"Sending {symbol} price information...")

    def calculatePeriod(self):
        time = 1000
        if self.selected_time_unit.get() == "seconds":
            time = int(self.spinbox_period.get()) * 1000
        elif self.selected_time_unit.get() == "minutes":
            time = int(self.spinbox_period.get()) * 1000 * 60
        elif self.selected_time_unit.get() == "hours":
            time = int(self.spinbox_period.get()) * 1000 * 60 * 60
        return time

    def deleteTask(self):
        (index_to_delete,) = self.listbox_tasks.curselection()
        del self.tasks[index_to_delete]
        
        temp_str_list = []
        if(self.tasks_string.get() != ""):
            temp_str_list = ast.literal_eval(self.tasks_string.get())
        temp_str_list = list(temp_str_list)
        del temp_str_list[index_to_delete]
        self.tasks_string.set(temp_str_list)
