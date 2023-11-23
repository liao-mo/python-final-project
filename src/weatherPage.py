import tkinter as tk


class WeatherPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Set the background color
        self.configure(bg="#010066")

        frame = tk.Frame(self, bg="#001F43", width=800, height=600)
        frame.propagate(False)
        frame.pack(pady=20)

        
        # Place label
        self.place_label = tk.Label(frame, text="Taipei")
        self.place_label.config(font=("Helvetica", 24), fg="#F6F7F8", bg="#5F4894", width=20)
        #self.place_label.pack(pady=10)
        self.place_label.grid(column=0, row=0, columnspan=4, sticky="ew", padx=200)

        # TMP label
        self.tmp_label = tk.Label(frame, text="21°")
        self.tmp_label.config(font=("Helvetica", 45), fg="#F6F7F8", bg="#5F4894")
        #self.tmp_label.pack(pady=10)
        self.tmp_label.grid(column=0,row=1, columnspan=4, sticky="ew", padx=200, pady=3)

        # Low label
        self.low_tmp_label = tk.Label(frame, text="最低:16°")
        self.low_tmp_label.config(font=("Helvetica", 15), fg="#F6F7F8", bg="#5F4894")
        #self.low_tmp_label.pack(pady=10)
        self.low_tmp_label.grid(column=0,row=2, columnspan=2, sticky="e", padx=5, pady=3)

        # High label
        self.high_tmp_label = tk.Label(frame, text="最高:27°")
        self.high_tmp_label.config(font=("Helvetica", 15), fg="#F6F7F8", bg="#5F4894")
        #self.high_tmp_label.pack(pady=10)
        self.high_tmp_label.grid(column=2,row=2, columnspan=2, sticky="w", padx=5, pady=3)
        

        
        # UV label frame
        self.uv_labelframe = tk.LabelFrame(frame, text="UV", fg="#F6F7F8", bg="#23274F", width=150, height=150)
        self.uv_labelframe.propagate(False)
        label1 = tk.Label(self.uv_labelframe, text="4", fg="#F6F7F8", bg="#23274F", font=("Helvetica", 30))
        label1.pack()

        # 体感温度 label frame
        self.feel_labelframe = tk.LabelFrame(frame, text="体感温度", fg="#F6F7F8", bg="#23274F", width=150, height=150)
        self.feel_labelframe.propagate(False)
        label2 = tk.Label(self.feel_labelframe, text="21°", fg="#F6F7F8", bg="#23274F", font=("Helvetica", 30))
        label2.pack()

        # Humidity label frame
        self.humid_labelframe = tk.LabelFrame(frame, text="湿度", fg="#F6F7F8", bg="#23274F", width=150, height=150)
        self.humid_labelframe.propagate(False)
        label3 = tk.Label(self.humid_labelframe, text="78%", fg="#F6F7F8", bg="#23274F", font=("Helvetica", 30))
        label3.pack()

        # Wind label frame
        self.wind_labelframe = tk.LabelFrame(frame, text="Wind", fg="#F6F7F8", bg="#23274F", width=150, height=150)
        self.wind_labelframe.propagate(False)
        label4 = tk.Label(self.wind_labelframe, text="2m/s", fg="#F6F7F8", bg="#23274F", font=("Helvetica", 30))
        label4.pack()

        self.uv_labelframe.grid(column=0,row=3, padx=25, pady=80)
        self.feel_labelframe.grid(column=1,row=3, padx=25, pady=80)
        self.humid_labelframe.grid(column=2,row=3, padx=25, pady=80)
        self.wind_labelframe.grid(column=3,row=3, padx=25, pady=80)
        