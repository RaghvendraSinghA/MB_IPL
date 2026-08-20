import matplotlib.pyplot as plt
from data import matches_list
from data import deliveries_list
from data import output_images_path


def calculate(matches_list,deliveries_list):


    match_ids_2016 = set()       #non-duplicate season 2016 match IDs.

    for match in matches_list:
        year = int(match["season"])

        if (year == 2016):
            match_ids_2016.add(match["id"])

    teams_extra_runs = {}

    for delivery in deliveries_list:
        id = delivery["match_id"]

        if id in match_ids_2016:
            team = delivery["bowling_team"]
            extra_runs = int(delivery["extra_runs"])

            if (team in teams_extra_runs.keys()):
                teams_extra_runs[team] += extra_runs
            else:
                teams_extra_runs[team] = extra_runs

    return teams_extra_runs


def plot(teams_extra_runs):

    plt.figure(figsize=(10,10))

    x_axis = teams_extra_runs.keys()
    y_axis = teams_extra_runs.values()

    bars=plt.bar(x_axis,y_axis)
        #called plt.show() here ,damn
    plt.xlabel("Teams")
    plt.ylabel("Extra runs conceded")
    plt.title("Extra runs conceded by each team in year 2016")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.bar_label(bars)

    plt.savefig(output_images_path/"q7_extra_runs_conceded_per_team_in_2016.png")
    plt.show()


def execute(matches_list,deliveries_list):
    teams_extra_runs = calculate(matches_list,deliveries_list)

    plot(teams_extra_runs)

    return teams_extra_runs

execute(matches_list,deliveries_list)
