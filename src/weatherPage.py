import tkinter as tk
from weather import *
from datetime import datetime, time


class WeatherPage(tk.Frame):
    def __init__(self, master, line_api_key):

        super().__init__(master)
        self.line_api_key = line_api_key

        # Set the background color
        self.configure(bg="#DEF1FA")

        frame = tk.Frame(self, bg="#DEF1FA", width=800, height=600)
        frame.propagate(False)
        frame.pack(pady=50)

        # Place label
        self.place_label = tk.Label(frame, text="Taipei")
        self.place_label.config(
            font=("Helvetica", 24), fg="#61798A", bg="#DEF1FA", width=20
        )
        self.place_label.grid(column=0, row=0, columnspan=4, sticky="ew", padx=200)

        # TMP label
        self.tmp_label = tk.Label(frame, text="{}°".format(get_temperature()))
        self.tmp_label.config(font=("Helvetica", 45), fg="#61798A", bg="#DEF1FA")
        self.tmp_label.grid(
            column=0, row=1, columnspan=4, sticky="ew", padx=200, pady=3
        )

        # Low label
        self.low_tmp_label = tk.Label(
            frame, text="最低:{}°".format(get_temperature_min())
        )
        self.low_tmp_label.config(font=("Helvetica", 15), fg="#61798A", bg="#DEF1FA")
        self.low_tmp_label.grid(
            column=0, row=2, columnspan=2, sticky="e", padx=5, pady=3
        )

        # High label
        self.high_tmp_label = tk.Label(
            frame, text="最高:{}°".format(get_temperature_max())
        )
        self.high_tmp_label.config(font=("Helvetica", 15), fg="#61798A", bg="#DEF1FA")
        self.high_tmp_label.grid(
            column=2, row=2, columnspan=2, sticky="w", padx=5, pady=3
        )

        # UV label frame
        self.uv_labelframe = tk.LabelFrame(
            frame, text="UV", fg="#61798A", bg="#B2DEFD", width=150, height=150
        )
        self.uv_labelframe.propagate(False)
        # UV value label
        self.label1 = tk.Label(
            self.uv_labelframe,
            text="{}".format(get_uv_value()),
            fg="#61798A",
            bg="#B2DEFD",
            font=("Helvetica", 30),
        )
        self.label1.pack()
        # UV image label
        self.uv_image = tk.PhotoImage(file="./images/ultraviolet-2.png")
        self.l_image = tk.Label(
            self.uv_labelframe, image=self.uv_image, width=80, height=80, bg="#B2DEFD"
        )
        self.l_image.image = self.uv_image
        self.l_image.pack()
        # UV check box
        self.uv_var = tk.BooleanVar()
        self.uv_var.set(False)
        self.uv_check = tk.Checkbutton(
            frame,
            text="UV",
            variable=self.uv_var,
            fg="#61798A",
            bg="#B2DEFD",
            selectcolor="#23274F",
        )
        self.uv_check.pack(pady=10)

        # 體感溫度 label frame
        self.feel_labelframe = tk.LabelFrame(
            frame, text="體感溫度", fg="#61798A", bg="#B2DEFD", width=150, height=150
        )
        self.feel_labelframe.propagate(False)
        # 體感溫度 value label
        self.label2 = tk.Label(
            self.feel_labelframe,
            text="{}°".format(get_feels_like()),
            fg="#61798A",
            bg="#B2DEFD",
            font=("Helvetica", 30),
        )
        self.label2.pack()
        # 體感溫度 image label
        self.feel_image = tk.PhotoImage(file="./images/temperature.png")
        self.l_image1 = tk.Label(
            self.feel_labelframe, image=self.feel_image, width=80, height=80, bg="#B2DEFD"
        )
        self.l_image1.image = self.feel_image
        self.l_image1.pack()
        # 體感溫度 check box
        self.feel_var = tk.BooleanVar()
        self.feel_var.set(False)
        self.feel_check = tk.Checkbutton(
            frame,
            text="Feel",
            variable=self.feel_var,
            fg="#61798A",
            bg="#B2DEFD",
            selectcolor="#23274F",
        )
        self.feel_check.pack(pady=10)

        # Humidity label frame
        self.humid_labelframe = tk.LabelFrame(
            frame, text="濕度", fg="#61798A", bg="#B2DEFD", width=150, height=150
        )
        self.humid_labelframe.propagate(False)
        # Humidity value label
        self.label3 = tk.Label(
            self.humid_labelframe,
            text="{}%".format(get_humidity()),
            fg="#61798A",
            bg="#B2DEFD",
            font=("Helvetica", 30),
        )
        self.label3.pack()
        # Humidity image label
        self.humid_image = tk.PhotoImage(file="./images/humidity.png")
        self.l_image2 = tk.Label(
            self.humid_labelframe, image=self.humid_image, width=80, height=80, bg="#B2DEFD"
        )
        self.l_image2.image = self.humid_image
        self.l_image2.pack()
        # Humidity check box
        self.humid_var = tk.BooleanVar()
        self.humid_var.set(False)
        self.humid_check = tk.Checkbutton(
            frame,
            text="Humidity",
            variable=self.humid_var,
            fg="#61798A",
            bg="#B2DEFD",
            selectcolor="#23274F",
        )
        self.humid_check.pack(pady=10)

        # Wind label frame
        self.wind_labelframe = tk.LabelFrame(
            frame, text="Wind", fg="#61798A", bg="#B2DEFD", width=150, height=150
        )
        self.wind_labelframe.propagate(False)
        # Wind value label
        self.label4 = tk.Label(
            self.wind_labelframe,
            text="{}m/s".format(get_wind_speed()),
            fg="#61798A",
            bg="#B2DEFD",
            font=("Helvetica", 30),
        )
        self.label4.pack()
        # Wind image label
        self.wind_image = tk.PhotoImage(file="./images/wind.png")
        self.l_image3 = tk.Label(
            self.wind_labelframe, image=self.wind_image, width=80, height=80, bg="#B2DEFD"
        )
        self.l_image3.image = self.wind_image
        self.l_image3.pack()
        # Wind check box
        self.wind_var = tk.BooleanVar()
        self.wind_var.set(False)
        self.wind_check = tk.Checkbutton(
            frame,
            text="Wind",
            variable=self.wind_var,
            fg="#61798A",
            bg="#B2DEFD",
            selectcolor="#23274F",
        )
        self.wind_check.pack(pady=10)

        # Place label frame
        self.uv_labelframe.grid(column=0, row=3, padx=25, pady=30)
        self.feel_labelframe.grid(column=1, row=3, padx=25, pady=30)
        self.humid_labelframe.grid(column=2, row=3, padx=25, pady=30)
        self.wind_labelframe.grid(column=3, row=3, padx=25, pady=30)

        # Place check box
        self.uv_check.grid(column=0, row=4, padx=25)
        self.feel_check.grid(column=1, row=4, padx=25)
        self.humid_check.grid(column=2, row=4, padx=25)
        self.wind_check.grid(column=3, row=4, padx=25)

        # set time entry
        self.entry = tk.Entry(self, width=10, fg="#61798A")
        self.entry.insert(0, "18:00")
        self.entry.pack(pady=3)

        # set time buttom
        self.set_button = tk.Button(
            self, text="Set", command=self.on_button_click, fg="#61798A"
        )
        # set_button.config(background="#B2DEFD")
        self.set_button.pack(pady=3)


    def weather_notify(self, uv, feel, humid, wind):
        # weather_notify()
        show_weather = "weather notification\n"
        if uv:
            show_weather += f"UV: {get_uv_value()}\n"
        if feel:
            show_weather += f"Feels like: {get_feels_like()} °C\n"
        if humid:
            show_weather += f"Humidity: {get_humidity()} %\n"
        if wind:
            show_weather += f"Wind: {get_wind_speed()} m/s\n"
        user = LineNotify(self.line_api_key)
        user.send_message(show_weather)
        print(show_weather)


    def on_button_click(self):
        # Show data
        entered_time = self.entry.get()
        entered_uv = self.uv_var.get()
        entered_feel = self.feel_var.get()
        entered_humid = self.humid_var.get()
        entered_wind = self.wind_var.get()
        print("Set time: " + entered_time)
        print("UV: " + str(entered_uv))
        print("Feel: " + str(entered_feel))
        print("Humidity: " + str(entered_humid))
        print("Wind: " + str(entered_wind))

        # 取得當前時間
        current_time = datetime.now().time()
        # 設定時間
        hour_min = entered_time.split(":")
        target_time = time(int(hour_min[0]), int(hour_min[1]), 0)
        # 計算距離設定時間還有多長時間
        time_difference = datetime.combine(
            datetime.today(), target_time
        ) - datetime.combine(datetime.today(), current_time)
        # 將時間轉換為毫秒
        delay_in_milliseconds = time_difference.total_seconds() * 1000
        # 使用after方法設定定時呼叫
        print("Waiting Time: " + str(time_difference.total_seconds()))
        self.after(
            int(delay_in_milliseconds),
            lambda: self.weather_notify(
                entered_uv, entered_feel, entered_humid, entered_wind
            ),
        )
