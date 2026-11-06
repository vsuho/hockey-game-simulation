
import time

class Team:
    def __init__(self, name: str, goals: int, is_home: bool) -> None:
        self.name = name
        self.goals = goals
        self.is_home = is_home

print("===== Welcome to tonight's game! =====")
time.sleep(1)

your_name = input("Choose your team: ")
opponent_name = input("Choose opponent team: ")

your_is_home: bool = input("Is your team at home? (y/n): ").strip().lower() == "y"

your_team = Team(your_name, 0, your_is_home)
opponent_team = Team(opponent_name, 0, not your_is_home)

time.sleep(0.5)
if your_team.is_home:
    print(f"\nGame on: {your_team.name} vs. {opponent_team.name} !\n")
else:
    print(f"\nGame on: {opponent_team.name} vs. {your_team.name} !\n")




