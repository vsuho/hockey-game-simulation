
import time

class Team:
    def __init__(self, name: str, is_home: bool) -> None:
        self.name = name
        self.is_home = is_home
        self.goals = 0

valid_teams: list = [
    "HIFK",
    "HPK",
    "Ilves",
    "Jokerit",
    "Jukurit",
    "JYP",
    "KalPa",
    "Kiekko-Espoo",
    "KooKoo",
    "Kärpät",
    "Lukko",
    "Pelicans",
    "SaiPa",
    "Sport",
    "Tappara",
    "TPS",
    "Ässät"
                     ]

def game():

    print("===== Welcome to tonight's Liiga game! =====")
    time.sleep(1)

    valid_teams_normalized = {team.casefold() for team in valid_teams}

    your_name = input("Choose your team: ")
    opponent_name = input("Choose opponent team: ")
    if your_name.lower() not in valid_teams_normalized or opponent_name.lower() not in valid_teams_normalized:
        print("Choose a valid Liiga team!")
        return 
        

    your_is_home: bool = input("Is your team at home? (y/n): ").strip().lower() == "y"

    your_team = Team(your_name, your_is_home)
    opponent_team = Team(opponent_name, not your_is_home)

    time.sleep(0.5)
    if your_team.is_home:
        print(f"\nGame on: {your_team.name} vs. {opponent_team.name} !\n")
    else:
        print(f"\nGame on: {opponent_team.name} vs. {your_team.name} !\n")

    period_length: int = 20

    def period(period_length):
        for i in range(0, period_length + 1):
            time.sleep(0.5)
            print(i)

game()




