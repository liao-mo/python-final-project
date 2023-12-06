import tkinter as tk
from lineNotify import *
from tkinter import ttk
import nba_live as nba_api

class NBAPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        
        # 目前選擇的兩隊撞到時會重複印
        def print_games():
            selected_teams = [team_listbox.get(index) for index in team_listbox.curselection()]
            dataSet = nba_api.getTodayScoreboard()
            if dataSet:
                for team in selected_teams:
                    for data in dataSet.data:
                        home_team_name = data["homeTeam"]["teamCity"] + " " + data["homeTeam"]["teamName"]
                        away_team_name = data["awayTeam"]["teamCity"] + " " + data["awayTeam"]["teamName"]
                        if home_team_name == team or away_team_name == team:
                            print(f"Home Team: {home_team_name}")
                            print(f"Away Team: {away_team_name}\n")
                            self.lineUser.send_message(f"Home Team: {home_team_name}")
                            self.lineUser.send_message(f"Away Team: {away_team_name}\n")
                            break

        def choose_teams():
            selected_teams = [team_listbox.get(index) for index in team_listbox.curselection()]
            team_label.config(text=f"Selected NBA Teams: {', '.join(selected_teams)}")
            print_games()

        def choose_time():
            selected_time = time_var.get()
            time_label.config(text=f"Selected Time: {selected_time}")
        
        self.lineUser = LineNotify()
        
        
        frame = tk.Frame(self, width=800, height=600)
        frame.propagate(False)
        # frame.pack(pady=50)
        frame.grid(column=4,row=5, padx=25, pady=30)
        
        
        # Set the background color
        # self.configure(bg="#81c994")

        self.entry_label = tk.Label(frame,text="NBA Helper")
        self.entry_label.config(font=("Helvetica", 24), bg="#81c994")
        # self.entry_label.pack(pady=10)
        self.entry_label.grid(row=0,column=2)
        

        # Create a list of NBA teams
        nba_teams = ["Atlanta Hawks", "Boston Celtics", "Brooklyn Nets", "Charlotte Hornets",
                    "Chicago Bulls", "Cleveland Cavaliers", "Dallas Mavericks", "Denver Nuggets",
                    "Detroit Pistons", "Golden State Warriors", "Houston Rockets", "Indiana Pacers",
                    "LA Clippers", "Los Angeles Lakers", "Memphis Grizzlies", "Miami Heat",
                    "Milwaukee Bucks", "Minnesota Timberwolves", "New Orleans Pelicans",
                    "New York Knicks", "Oklahoma City Thunder", "Orlando Magic", "Philadelphia 76ers",
                    "Phoenix Suns", "Portland Trail Blazers", "Sacramento Kings", "San Antonio Spurs",
                    "Toronto Raptors", "Utah Jazz", "Washington Wizards"]

        # Create a Listbox with Scrollbar for NBA teams (allow multiple selections)
        team_listbox = tk.Listbox(frame, selectmode=tk.MULTIPLE,)
        # team_listbox.pack(side=tk.LEFT, padx=10)
        team_listbox.grid(column=0,row=0)
        
        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=team_listbox.yview)
        # scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        scrollbar.grid(row=0, column=1, sticky='ns')
        team_listbox.config(yscrollcommand=scrollbar.set)
        for team in nba_teams:
            team_listbox.insert(tk.END, team)

        # Create a button to choose NBA teams
        choose_teams_button = tk.Button(frame, text="Choose Teams", command=choose_teams)
        # choose_teams_button.pack(pady=10)
        choose_teams_button.grid(row=1,column=2)

        # Create a Label for displaying the selected NBA teams
        team_label = tk.Label(frame, text="Selected NBA Teams: ")
        # team_label.pack(pady=10)
        team_label.grid(row=2,column=2)
        
        # Create a Combobox for selecting time
        time_var = tk.StringVar()
        time_combobox = ttk.Combobox(frame, textvariable=time_var, values=["6:00 PM", "7:00 PM", "8:00 PM", "9:00 PM"])
        # time_combobox.pack(pady=10)
        time_combobox.grid(row=3,column=2)
        
        # Create a button to choose time
        choose_time_button = tk.Button(frame, text="Choose Time", command=choose_time)
        # choose_time_button.pack(pady=10)
        choose_time_button.grid(row=4,column=2)

        # Create a Label for displaying the selected time
        time_label = tk.Label(frame, text="Selected Time: ")
        # time_label.pack(pady=10)
        time_label.grid(row=5,column=2)

