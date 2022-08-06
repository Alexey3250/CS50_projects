# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000

# How teams are represented: {"team": "Uruguay", "rating": 976}.


def main():

    # ensure that len(sys.argv) (the number of command-line arguments) is 2.
    # We’ll use command-line arguments to tell Python which team CSV file to use to run the tournament simulation.
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    # We’ve then defined a list called teams (which will eventually be a list of teams) and a dictionary called counts
    # (which will associate team names with the number of times that team won a simulated tournament).
    teams = []  # each team should be a dictionary with a team name and a rating.
    filename = sys.argv[1]
    with open(filename) as f:
        # cerates an object in Python that you can loop over to read the file one row at a time, treating each row as a dictionary.
        reader = csv.DictReader(f)
        for team in reader:
            # "rating" - acessing the key of the table; then casting integer there
            team["rating"] = int(team["rating"])
            teams.append(team)

    # we sort the teams in descending order of how many times they won simulations (according to counts)
    # and print the estimated probability that each team wins the World Cup.
    counts = {}
    for i in range(N):
        winner = simulate_tournament(teams)
        if winner in counts:
            counts[winner] += 1
        else:
            counts[winner] = 1

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")

# The simulate_game function accepts two teams as inputs (recall that each team is a dictionary containing the team name and the team’s rating),
#  and simulates a game between them. If the first team wins, the function returns True; otherwise, the function returns False.


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability

# The simulate_round function accepts a list of teams (in a variable called teams) as input,
#  and simulates games between each pair of teams. The function then returns a list of all of the teams that won the round.


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    while len(teams) > 1:
        teams = simulate_round(teams)
    return teams[0]["team"]


if __name__ == "__main__":
    main()
