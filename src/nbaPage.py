import tkinter as tk
from lineNotify import *
import nba_live as nba_live
from datetime import datetime, timezone, timedelta
from dateutil import parser,tz


class NBAPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.interval_days = 0
        
        self.lineUser = LineNotify()

        frame = tk.Frame(self, width=800, height=600)
        frame.propagate(False)
        frame.pack(pady=10)
        
        self.entry_label = tk.Label(frame, text="NBA Schedule Assistant")
        self.entry_label.config(font=("Helvetica", 24), bg="#81c994")
        self.entry_label.grid(row=0,column=0,columnspan=8,sticky="ew")
        
        self.firstline = tk.Label(frame, text="    All NBA Teams:")
        self.firstline.config(font=("Helvetica", 14))
        self.firstline.grid(row=1, column=0, columnspan=2,padx=20)
        

        # a list of NBA teams
        nba_teams = ["Atlanta Hawks", "Boston Celtics", "Brooklyn Nets", "Charlotte Hornets",
                     "Chicago Bulls", "Cleveland Cavaliers", "Dallas Mavericks", "Denver Nuggets",
                     "Detroit Pistons", "Golden State Warriors", "Houston Rockets", "Indiana Pacers",
                     "LA Clippers", "Los Angeles Lakers", "Memphis Grizzlies", "Miami Heat",
                     "Milwaukee Bucks", "Minnesota Timberwolves", "New Orleans Pelicans",
                     "New York Knicks", "Oklahoma City Thunder", "Orlando Magic", "Philadelphia 76ers",
                     "Phoenix Suns", "Portland Trail Blazers", "Sacramento Kings", "San Antonio Spurs",
                     "Toronto Raptors", "Utah Jazz", "Washington Wizards"]

        # Create a Listbox with Scrollbar for NBA teams (allow multiple selections)
        self.team_listbox = tk.Listbox(frame, selectmode=tk.MULTIPLE,)
        self.team_listbox.config(font=("Helvetica", 10))
        self.team_listbox.grid(row=2,column=0,columnspan=2,sticky="nsew")

        self.scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=self.team_listbox.yview)

        self.scrollbar.grid(row=2, column=2, sticky='nsw')
        self.team_listbox.config(yscrollcommand=self.scrollbar.set)
        for team in nba_teams:
            self.team_listbox.insert(tk.END, team)
            

        self.choose_all_teams_button = tk.Button(frame, text="Select All", command=self.select_all_teams)
        self.choose_all_teams_button.config(font=("Helvetica", 10))
        self.choose_all_teams_button.grid(row=3, column=0,columnspan=2,sticky="ew")
        
        # Create a button to choose NBA teams
        self.choose_teams_button = tk.Button(frame, text="Choose Teams", command=self.choose_teams)
        self.choose_teams_button.config(font=("Helvetica", 10))
        self.choose_teams_button.grid(row=3, column=2,columnspan=3,sticky="ew")
        

        self.choose_all_teams_button = tk.Button(frame, text="Clear All", command=self.clear_all_teams)
        self.choose_all_teams_button.config(font=("Helvetica", 10))
        self.choose_all_teams_button.grid(row=3, column=5,columnspan=2,sticky="ew")
        
        
        self.image_labelframe = tk.LabelFrame(frame, fg="#61798A", bg="#B2DEFD", width=300, height=200)
        self.image_labelframe.propagate(False)
        self.arrows_image = tk.PhotoImage(file="./images/arrows.png")
        
        self.image_label = tk.Label(self.image_labelframe,image=self.arrows_image,width=300,height=200)
        self.image_label.pack()
        
        self.image_labelframe.grid(row=2, column=2,columnspan=3,sticky="w",padx=20)

        # Create a Label for displaying the selected NBA teams
        self.selected_team_label = tk.Label(frame, text="Your Selected Teams:   ")
        self.selected_team_label.config(font=("Helvetica", 14))
        self.selected_team_label.grid(row=1, column=5, columnspan=2,sticky="w")
        
        self.team_label = tk.Label(frame, text="None")
        self.team_label.config(font=("Helvetica", 14))
        self.team_label.grid(row=2, column=5, columnspan=2,sticky="nsew")

        self.freeline= tk.Label(frame, text="------------------------------------------------------------------------------------------------------------------------------------------------------")
        self.freeline.grid(row=4, column=0,columnspan=8,sticky="ew")
        
        self.service1_label = tk.Label(frame, text="> Service 1 : Directly send today's schedule and game status.")
        self.service1_label.config(font=("Helvetica", 14))
        self.service1_label.grid(row=5, column=0,columnspan=5,sticky="w")
        
        self.send_today_schedule_button = tk.Button(frame, text="Send", command=self.send_today_schedule)
        self.send_today_schedule_button.config(font=("Helvetica", 14), bg="#fff5f5")
        self.send_today_schedule_button.grid(row=5, rowspan=2, column=6,sticky="ew")
        
        self.sent_signal_label = tk.Label(frame, text="Not sent yet...")
        self.sent_signal_label.config(font=("Helvetica", 12))
        self.sent_signal_label.grid(row=6, column=1,columnspan=4,sticky="ew")
        
        self.service2_label = tk.Label(frame, text="> Service 2 : Periodically send the schedule in the near future.")
        self.service2_label.config(font=("Helvetica", 14))
        self.service2_label.grid(row=7, column=0,columnspan=6,sticky="w",pady=5)
        
        self.setting_label = tk.Label(frame, text="-> Select schedule in: ")
        self.setting_label.config(font=("Helvetica", 12))
        self.setting_label.grid(row=8, column=0, columnspan=2, sticky="w", padx=20)
        
        self.time_symbols = ["1 day", "2 days", "3 days", "1 week"]
        self.selected_time_symbol = tk.StringVar()
        self.selected_time_symbol.set("choose")

        self.menu_symbols = tk.OptionMenu(frame, self.selected_time_symbol, *self.time_symbols)
        self.menu_symbols.config(font=("Helvetica", 12))
        self.menu_symbols.grid(row=8, column=2, pady=10, padx=5)
        
        # cause strange problem
        # self.setting2_label = tk.Label(frame, text="-> Select sending period: ")
        # self.setting2_label.grid(row=9, column=1)
        
        self.setting2_label = tk.Label(frame, text="-> Select sending period: ")
        self.setting2_label.config(font=("Helvetica", 12))
        self.setting2_label.grid(row=9, column=0, columnspan=2, sticky="w", padx=20)
        
        self.hours_period = tk.Spinbox(frame, from_=0, to=128, width=5)
        self.hours_period.config(font=("Helvetica", 16), bg="#fff5f5")
        self.hours_period.grid(row=9, column=2, padx=5)
        self.minutes_period = tk.Spinbox(frame, from_=0, to=60, width=5)
        self.minutes_period.config(font=("Helvetica", 16), bg="#fff5f5")
        self.minutes_period.grid(row=9, column=3, padx=5)
        self.seconds_period = tk.Spinbox(frame, from_=0, to=60, width=5)
        self.seconds_period.config(font=("Helvetica", 16), bg="#fff5f5")
        self.seconds_period.grid(row=9, column=4, padx=5)
        
        self.hours_label = tk.Label(frame, text="hours")
        self.minutes_label = tk.Label(frame, text="minutes")
        self.seconds_label = tk.Label(frame, text="seconds")
        
        # Arrange Entry widgets and Labels in a row
        self.hours_label.grid(row=11, column=2, sticky="ew")
        self.minutes_label.grid(row=11, column=3, sticky="ew")
        self.seconds_label.grid(row=11, column=4, sticky="ew")

        # Create a button to convert and trigger messaging
        self.trigger_button = tk.Button(frame, text="Activate", command=self.convert_and_trigger)
        self.trigger_button.config(font=("Helvetica", 14), bg="#fff5f5")
        self.trigger_button.grid(row=8, rowspan=3, column=6,sticky="nsew")
        
        self.activated_signal_label = tk.Label(frame, text="Not activate yet...")
        self.activated_signal_label.config(font=("Helvetica", 12))
        self.activated_signal_label.grid(row=13, column=1,columnspan=4,sticky="ew")
        

        
    def makeTeamFullName(self, teamCity, teamName):
        teamFullName = teamCity + " " + teamName
        return teamFullName
        

    def send_today_schedule(self):
        selected_teams = [self.team_listbox.get(index) for index in self.team_listbox.curselection()]
        dataSet = nba_live.getTodayScoreboard()
        if dataSet:
            redundantTeams = []
            
            for team in selected_teams:
                if team not in redundantTeams:
                    for data in dataSet.data:
                        home_team_name = self.makeTeamFullName(data["homeTeam"]["teamCity"], data["homeTeam"]["teamName"])
                        away_team_name = self.makeTeamFullName(data["awayTeam"]["teamCity"], data["awayTeam"]["teamName"])
                        
                        if home_team_name == team or away_team_name == team:
                            game_status = data["gameStatusText"]
                            self.lineUser.send_message(f"Home Team:\n{home_team_name}\nAway Team:\n{away_team_name}\nGame Status: {game_status}")
                            
                            redundantTeams.append(home_team_name)
                            redundantTeams.append(away_team_name)
                            self.sent_signal_label.config(text="Sent successfully!")
                            break
                    
               
    # if the number of days from now to the designated games are less then dayslimit, the game info should be send to line
    def sendGamesSchedule(self, schedule, dayslimit):
        current_time_utc = datetime.now(timezone.utc)
        print(current_time_utc)
        
        # Extracting homeTeam and awayTeam for each game
        for game_date in schedule["leagueSchedule"]["gameDates"]:
            redundantTeams = []
            for game in game_date["games"]:
                
                # Parsing game time in UTC
                game_time_dt = parser.parse(game["gameDateTimeUTC"])
                # Converting to a specific timezone, for example, UTC
                game_time_utc = game_time_dt.replace(tzinfo=tz.tzutc())
                # Calculate days between 
                daysbetween = int(((game_time_utc-current_time_utc).total_seconds())//(3600*24))
                        
                if daysbetween <= dayslimit and daysbetween >=0:
                    selected_teams = set(self.team_listbox.get(index) for index in self.team_listbox.curselection()) - set(redundantTeams)
                    
                    for team in selected_teams:
                        home_team_name = self.makeTeamFullName(game["homeTeam"]["teamCity"], game["homeTeam"]["teamName"])
                        away_team_name = self.makeTeamFullName(game["awayTeam"]["teamCity"], game["awayTeam"]["teamName"])
                        
                        if home_team_name == team or away_team_name == team:

                            current_time_taiwan = game_time_utc.astimezone(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M")
                            print(f"Home Team: {home_team_name}")
                            print(f"Away Team: {away_team_name}\n")
                            
                            self.lineUser.send_message(f"\n{daysbetween} days left!\nHome Team:\n{home_team_name}\nAway Team:\n{away_team_name}\n{current_time_taiwan}")
                            
                            redundantTeams.append(home_team_name)
                            redundantTeams.append(away_team_name)
                            break
                            
                            
                

    def choose_teams(self):
        selected_teams = [self.team_listbox.get(index) for index in self.team_listbox.curselection()]
        self.team_label.config(text="\n{}".format('\n'.join(selected_teams)))
        self.sent_signal_label.config(text="Selected teams changed! Not sent yet...")
        
        
    def choose_time(self):
        selected_time = self.selected_time_symbol.get()
        interval_days_mapping = {"1 day": 1, "2 days": 2, "3 days": 3, "1 week": 7}
        
        try:
            self.interval_days = interval_days_mapping[selected_time]
            
        except KeyError:
            # Handle the case where selected_time is not in the mapping
            print("Invalid selection")



    def send_messages_periodically(self, interval_seconds):
        self.sendGamesSchedule(nba_live.getSchedule(), self.interval_days)
        self.after(interval_seconds, self.send_messages_periodically, interval_seconds)
        
    def convert_and_trigger(self):
        self.choose_time()
        
        try:
            # Get the values entered by the user in hours, minutes, and seconds entries
            hours = int(self.hours_period.get())
            minutes = int(self.minutes_period.get())
            seconds = int(self.seconds_period.get())

            # Convert the total time to seconds
            seconds_interval = (hours * 3600 + minutes * 60 + seconds) * 1000
            if (seconds_interval <= 0):
                raise ValueError("Only positive values are allowed.")
            
            # Use lineUser to send messages every seconds_interval
            self.send_messages_periodically(seconds_interval)
            self.activated_signal_label.config(text="Activated successfully!")

        except ValueError:
            # Handle the case where user enters non-numeric values
            print("Invalid input. Please enter numeric values for hours, minutes, and seconds.")
            
    def select_all_teams(self):
        for team in range(self.team_listbox.size()):
            self.team_listbox.selection_set(team)
    
    
    def clear_all_teams(self):
        self.team_listbox.selection_clear(0, tk.END)