import time
import random

class Team:
    def __init__(self, name: str, is_home: bool) -> None:
        self.name = name
        self.shots_on_goal = 0
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

def period(length: int, home_team: Team, away_team: Team) -> tuple[int, int]:
        possibility_of_goal = 0.05

        # For each minute in the simulation
        for minute in range(0, length + 1):
            time.sleep(0.5)
            print(f"{minute} minutes played in the period")

            if random.random() < possibility_of_goal:
                scoring_team = random.choice([home_team, away_team])
                scoring_team.goals += 1
                print(f"GOAL! {scoring_team.name} "
                    f"({home_team.goals} - {away_team.goals})"
                )

        return (home_team.goals, away_team.goals)

def shootout(home_team: Team, away_team: Team) -> None:
    # Heads or tails guess to pick who goes first
    your_choice = input("Let's pick which team goes first. Heads or tails? (h/t) : ").casefold()
    if your_choice == "h":
        print("You picked heads.")
    elif your_choice == "t":
        print("You picked tails.")
    else:
        print("Type h or t")
        return

    print("Let's toss the coin: ")

    coin_toss = random.choice(("h", "t"))
    print(f"The coin landed on {'heads' if coin_toss == 'h' else 'tails'}.")

    first_team = home_team if coin_toss == "h" else away_team
    print(f"{first_team.name} goes first.")



    



def game_preparations() -> tuple[Team, Team]:

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

    home_team, away_team = (
        (your_team, opponent_team) if your_is_home else (opponent_team, your_team)
    )

    time.sleep(0.5)

    if your_team.is_home:
        print(f"\nGame on: {your_team.name} vs. {opponent_team.name}\n")
    else:
        print(f"\nGame on: {opponent_team.name} vs. {your_team.name}\n")

    return (home_team, away_team)

def full_game(home_team: Team, away_team: Team) -> None:
    # Three periods
    for period_number in range(1, 4):
        print(f"\nPeriod {period_number}\n")
        period(20, home_team, away_team)
        print(f"\nPeriod {period_number} over:\n Score: {home_team.goals} - {away_team.goals}")
        if period_number < 3: print(f"\n Heading to period {period_number + 1}...")

        if period_number < 3:
            time.sleep(2)

    # After three periods: check if game is not tied 
    if home_team.goals != away_team.goals:    
        print(f"\n ====== FINAL SCORE: {home_team.name} {home_team.goals} -"
            f" {away_team.goals} {away_team.name} ====== \n"
            )
        
        # Game is tied after 60, overtime begins
    else:
        print(f"Game is tied at {home_team.goals} - {away_team.goals}, heading to overtime...")
        time.sleep(5)
        period(5, home_team, away_team)

home_team, away_team = game_preparations()
final_result = full_game(home_team, away_team)
#shootout(home_team, away_team)

