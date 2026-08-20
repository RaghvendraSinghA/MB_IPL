import matplotlib.pyplot as plt
from data import deliveries_list

from data import output_images_path


def calculate(deliveries_list):

    rcb_players_scores = {}


    for ball in deliveries_list:
        team = ball["batting_team"]

        if(team == "Royal Challengers Bangalore"):
            player = ball["batsman"]
            runs = int(ball["batsman_runs"])

            if(player in rcb_players_scores):
                rcb_players_scores[player] +=runs
            else:
                rcb_players_scores[player] = runs


    rcb_players_scores_list = []

    for player in rcb_players_scores:
        name_and_runs ={}
        name_and_runs["name"] = player
        name_and_runs["runs"] = rcb_players_scores[player]

        rcb_players_scores_list.append(name_and_runs)

        rcb_players_scores_list.sort(key = lambda obj : obj["runs"],reverse = True)

    return  rcb_players_scores_list[0:10]


def plot(rcb_topten_players):
    plt.figure(figsize=(10,10))

    plt.xlabel("Players")
    plt.ylabel("Runs")
    plt.title("Top ten run scorers of RCB")
    plt.xticks(rotation=90)

    names = []
    runs = []

    for player in rcb_topten_players:
        names.append(player["name"])
        runs.append(player["runs"])

    bars = plt.bar(names,runs)

    plt.bar_label(bars)

    plt.tight_layout()

    plt.savefig(output_images_path/"q2_top_10_run_scorers_of_rcb.png")
    plt.show()




def execute(deliveries_list):
    rcb_topten_players = calculate(deliveries_list)
    plot(rcb_topten_players)
    return rcb_topten_players

execute(deliveries_list)