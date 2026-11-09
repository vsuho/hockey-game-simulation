
import time

class Team:
    def __init__(self, name: str, shots_on_goal: int, is_home: bool) -> None:
        self.name = name
        self.shots_on_goal = shots_on_goal
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

def period(length: int):
        for i in range(0, length + 1):
            time.sleep(0.5)
            print(i)

def game():

    print("\n===== Welcome to tonight's Liiga game! =====\n")
    time.sleep(1)

    valid_teams_normalized = {team.casefold() for team in valid_teams}

    # If both teams are valid, break while loop and continue executing, else print an error message
    while True:
        your_name = input("Choose your team: ").strip()
        opponent_name = input("Choose opponent team: ").strip()

        if (
            your_name.casefold() in valid_teams_normalized
            and opponent_name.casefold() in valid_teams_normalized
        ):
            break

        time.sleep(0.2)
        print("\nChoose a valid Liiga team!\n")
        
    your_is_home: bool = input("Is your team at home? (y/n): ").casefold() == "y"

    your_team = Team(your_name, your_is_home)
    opponent_team = Team(opponent_name, not your_is_home)

    time.sleep(0.5)

    if your_team.is_home:
        print(f"\nGame on: {your_team.name} vs. {opponent_team.name} !\n")
    else:
        print(f"\nGame on: {opponent_team.name} vs. {your_team.name} !\n")

game()
period(20)