# import requests
# # import nba_api
# from nba_api.stats.endpoints import scoreboard

# re=requests.get("https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json")

# print(scoreboard.Scoreboard().get_json())

from nba_api.live.nba.endpoints._base import Endpoint
from nba_api.live.nba.library.http import NBALiveHTTP


class ScoreBoard(Endpoint):
    endpoint_url = "scoreboard/todaysScoreboard_00.json"
    expected_data = {
        "meta": {"version": 0, "request": "", "time": "", "code": 0},
        "scoreboard": {
            "gameDate": "",
            "leagueId": "",
            "leagueName": "",
            "games": [
                {
                    "gameId": "",
                    "gameCode": "",
                    "gameStatus": 0,
                    "gameStatusText": "",
                    "period": 0,
                    "gameClock": "",
                    "gameTimeUTC": "",
                    "gameEt": "",
                    "regulationPeriods": 0,
                    "seriesGameNumber": "",
                    "seriesText": "",
                    "homeTeam": {
                        "teamId": 0,
                        "teamName": "",
                        "teamCity": "",
                        "teamTricode": "",
                        "wins": 0,
                        "losses": 0,
                        "score": 0,
                        "inBonus": None,
                        "timeoutsRemaining": 0,
                        "periods": [{"period": 0, "periodType": "", "score": 0}],
                    },
                    "awayTeam": {
                        "teamId": 0,
                        "teamName": "",
                        "teamCity": "",
                        "teamTricode": "",
                        "wins": 0,
                        "losses": 0,
                        "score": 0,
                        "inBonus": None,
                        "timeoutsRemaining": 0,
                        "periods": [{"period": 0, "periodType": "", "score": 0}],
                    },
                    "gameLeaders": {
                        "homeLeaders": {
                            "personId": 0,
                            "name": "",
                            "jerseyNum": "",
                            "position": "",
                            "teamTricode": "",
                            "playerSlug": None,
                            "points": 0,
                            "rebounds": 0,
                            "assists": 0,
                        },
                        "awayLeaders": {
                            "personId": 0,
                            "name": "",
                            "jerseyNum": "",
                            "position": "",
                            "teamTricode": "",
                            "playerSlug": None,
                            "points": 0,
                            "rebounds": 0,
                            "assists": 0,
                        },
                    },
                    "pbOdds": {"team": None, "odds": 0.0, "suspended": 0},
                }
            ],
        },
    }

    nba_response = None
    data_sets = None
    score_board_date = None
    games = None
    headers = None

    def __init__(self, proxy=None, headers=None, timeout=30, get_request=True):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        if get_request:
            self.get_request()

    def get_request(self):
        self.nba_response = NBALiveHTTP().send_api_request(
            endpoint=self.endpoint_url,
            parameters={},
            proxy=self.proxy,
            headers=self.headers,
            timeout=self.timeout,
        )
        self.load_response()

    def load_response(self):
        data_sets = self.nba_response.get_dict()
        if "scoreboard" in data_sets:
            self.score_board_date = data_sets["scoreboard"]["gameDate"]
            if "games" in data_sets["scoreboard"]:
                self.games = Endpoint.DataSet(data=data_sets["scoreboard"]["games"])


def getTodayScoreboard():
    # Create an instance of the ScoreBoard class
    scoreboard_instance = ScoreBoard()

    # Access data from the instance
    game_date = scoreboard_instance.score_board_date
    games = scoreboard_instance.games

    # Example: Print the game date and details of the first game
    print("Game Date:", game_date)

    # print(games.data)
    # if games:
    #     for data in games.data:
    #         # ori: first_game = games.data[0]
    #         first_game = data
    #         home_team_name = first_game["homeTeam"]["teamCity"] + first_game["homeTeam"]["teamName"]
    #         away_team_name = first_game["awayTeam"]["teamCity"] + first_game["awayTeam"]["teamName"]
    #         print("First Game Details:")
    #         print(f"Home Team: {home_team_name}")
    #         print(f"Away Team: {away_team_name}")
    #         print("//////////////////////////////////////////////////////////////////////")
    
    return games
        

# # You can also access other properties and methods of the instance as needed
# # Example: Access the raw NBA API response
# raw_response = scoreboard_instance.nba_response._response
# print("\n\nRaw NBA API Response:", raw_response)
