import tkinter as tk
from weather import *


class WeatherPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Set the background color
        self.configure(bg="#DEF1FA")

        frame = tk.Frame(self, bg="#DEF1FA", width=800, height=600)
        frame.propagate(False)
        frame.pack(pady=50)

        
        # Place label
        self.place_label = tk.Label(frame, text="Taipei")
        self.place_label.config(font=("Helvetica", 24), fg="#61798A", bg="#DEF1FA", width=20)
        #self.place_label.pack(pady=10)
        self.place_label.grid(column=0, row=0, columnspan=4, sticky="ew", padx=200)

        # TMP label
        self.tmp_label = tk.Label(frame, text="{}°".format(get_temperature()))
        self.tmp_label.config(font=("Helvetica", 45), fg="#61798A", bg="#DEF1FA")
        #self.tmp_label.pack(pady=10)
        self.tmp_label.grid(column=0,row=1, columnspan=4, sticky="ew", padx=200, pady=3)

        # Low label
        self.low_tmp_label = tk.Label(frame, text="最低:{}°".format(get_temperature_min()))
        self.low_tmp_label.config(font=("Helvetica", 15), fg="#61798A", bg="#DEF1FA")
        #self.low_tmp_label.pack(pady=10)
        self.low_tmp_label.grid(column=0,row=2, columnspan=2, sticky="e", padx=5, pady=3)

        # High label
        self.high_tmp_label = tk.Label(frame, text="最高:{}°".format(get_temperature_max()))
        self.high_tmp_label.config(font=("Helvetica", 15), fg="#61798A", bg="#DEF1FA")
        #self.high_tmp_label.pack(pady=10)
        self.high_tmp_label.grid(column=2,row=2, columnspan=2, sticky="w", padx=5, pady=3)
        

        
        # UV label frame
        self.uv_labelframe = tk.LabelFrame(frame, text="UV", fg="#61798A", bg="#B2DEFD", width=150, height=150)
        self.uv_labelframe.propagate(False)
        # UV value label
        label1 = tk.Label(self.uv_labelframe, text="{}".format(get_uv_value()), fg="#61798A", bg="#B2DEFD", font=("Helvetica", 30))
        label1.pack()
        # UV image label
        uv_image = tk.PhotoImage(file="./images/ultraviolet-2.png")
        l_image = tk.Label(self.uv_labelframe, image=uv_image, width=80, height=80, bg="#B2DEFD")
        l_image.image = uv_image
        l_image.pack()
        # UV check box
        uv_var = tk.BooleanVar()
        uv_var.set(False)
        uv_check = tk.Checkbutton(frame, text="UV", variable=uv_var, fg="#61798A", bg="#B2DEFD", selectcolor="#23274F")
        uv_check.pack(pady=10)

        # 体感温度 label frame
        self.feel_labelframe = tk.LabelFrame(frame, text="体感温度", fg="#61798A", bg="#B2DEFD", width=150, height=150)
        self.feel_labelframe.propagate(False)
        # 体感温度 value label
        label2 = tk.Label(self.feel_labelframe, text="{}°".format(get_feels_like()), fg="#61798A", bg="#B2DEFD", font=("Helvetica", 30))
        label2.pack()
        # 体感温度 image label
        feel_image = tk.PhotoImage(file="./images/temperature.png")
        l_image1 = tk.Label(self.feel_labelframe, image=feel_image, width=80, height=80, bg="#B2DEFD")
        l_image1.image = feel_image
        l_image1.pack()
        # 体感温度 check box
        feel_var = tk.BooleanVar()
        feel_var.set(False)
        feel_check = tk.Checkbutton(frame, text="Feel", variable=feel_var, fg="#61798A", bg="#B2DEFD", selectcolor="#23274F")
        feel_check.pack(pady=10)

        # Humidity label frame
        self.humid_labelframe = tk.LabelFrame(frame, text="湿度", fg="#61798A", bg="#B2DEFD", width=150, height=150)
        self.humid_labelframe.propagate(False)
        # Humidity value label
        label3 = tk.Label(self.humid_labelframe, text="{}%".format(get_humidity()), fg="#61798A", bg="#B2DEFD", font=("Helvetica", 30))
        label3.pack()
        # Humidity image label
        humid_image = tk.PhotoImage(file="./images/humidity.png")
        l_image2 = tk.Label(self.humid_labelframe, image=humid_image, width=80, height=80, bg="#B2DEFD")
        l_image2.image = humid_image
        l_image2.pack()
        # Humidity check box
        humid_var = tk.BooleanVar()
        humid_var.set(False)
        humid_check = tk.Checkbutton(frame, text="Humidity", variable=humid_var, fg="#61798A", bg="#B2DEFD", selectcolor="#23274F")
        humid_check.pack(pady=10)

        # Wind label frame
        self.wind_labelframe = tk.LabelFrame(frame, text="Wind", fg="#61798A", bg="#B2DEFD", width=150, height=150)
        self.wind_labelframe.propagate(False)
        # Wind value label
        label4 = tk.Label(self.wind_labelframe, text="{}m/s".format(get_wind_speed()), fg="#61798A", bg="#B2DEFD", font=("Helvetica", 30))
        label4.pack()
        # Wind image label
        wind_image = tk.PhotoImage(file="./images/wind.png")
        l_image3 = tk.Label(self.wind_labelframe, image=wind_image, width=80, height=80, bg="#B2DEFD")
        l_image3.image = wind_image
        l_image3.pack()
        # Wind check box
        wind_var = tk.BooleanVar()
        wind_var.set(False)
        wind_check = tk.Checkbutton(frame, text="Wind", variable=wind_var, fg="#61798A", bg="#B2DEFD", selectcolor="#23274F")
        wind_check.pack(pady=10)

        # Place label frame
        self.uv_labelframe.grid(column=0,row=3, padx=25, pady=30)
        self.feel_labelframe.grid(column=1,row=3, padx=25, pady=30)
        self.humid_labelframe.grid(column=2,row=3, padx=25, pady=30)
        self.wind_labelframe.grid(column=3,row=3, padx=25, pady=30)

        # Place check box
        uv_check.grid(column=0,row=4, padx=25)
        feel_check.grid(column=1,row=4, padx=25)
        humid_check.grid(column=2,row=4, padx=25)
        wind_check.grid(column=3,row=4, padx=25)
        
        # Setting time
        def on_button_click():
            entered_text = entry.get()
            print("入力されたテキスト: " + entered_text)

        # Entryウィジェットを作成
        entry = tk.Entry(self, width=10, fg="#61798A")
        entry.insert(0, "18:00")
        entry.pack(pady=3)

        # ボタンを作成
        set_button = tk.Button(self, text="Set", command=on_button_click, fg="#61798A")
        #set_button.config(background="#B2DEFD")
        set_button.pack(pady=3)