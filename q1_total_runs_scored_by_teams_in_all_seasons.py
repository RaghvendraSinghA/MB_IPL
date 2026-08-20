"""Calculate and plot total runs scored by teams in all IPL seasons."""

import matplotlib.pyplot as plt

from data import deliveries_list
from data import output_images_path


def calculate(deliveries_list):
    grouped_teams = {}  # dictionary to group team with their total runs in all seasons.

    for ball in deliveries_list:
        team = ball["batting_team"]
        run = int(ball["total_runs"])

        if team in grouped_teams:
            grouped_teams[team] = grouped_teams[team] + run
        else:
            grouped_teams[team] = run

    return grouped_teams


def plot(grouped_team):
    plt.figure(figsize=(10, 10))

    plt.xlabel("Teams")
    plt.ylabel("Total runs")
    plt.title("Total runs scored by teams in all seasons")

    plt.xticks(rotation=90)

    bars = plt.bar(grouped_team.keys(), grouped_team.values())
    plt.bar_label(bars)  # It needs object returned by plt.bar()
    # that object looks like Array of arrayofkeys and arrayofvals.

    plt.tight_layout()
    plt.savefig(output_images_path / "q1_total_runs_scored_by_teams_in_all_seasons.png")
    plt.show()


def execute(deliveries_list):
    grouped_teams = calculate(deliveries_list)
    # It calculates data and returns group of teams in deictionary.

    plot(grouped_teams)  # It plots data in chart by taking grouped_team data in argument.

    return grouped_teams


execute(deliveries_list)
