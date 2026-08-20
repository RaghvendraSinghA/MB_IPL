import matplotlib.pyplot as plt
from data import matches_list
from data import deliveries_list
from data import output_images_path


def calculate(matches_list,deliveries_list):

    match_ids_2015 = set()

    for match in matches_list:
        year = int(match["season"])

        if (year == 2015):
            match_ids_2015.add(match["id"])


    bowlers_runs_in_2015 = {}

    for delivery in deliveries_list:
        id = delivery["match_id"]

        if id in match_ids_2015:
            bowler = delivery["bowler"]
            runs = int(delivery["total_runs"])

            if bowler in bowlers_runs_in_2015.keys():
                bowlers_runs_in_2015[bowler]["run"] += runs
                bowlers_runs_in_2015[bowler]["balls"] += 1
            else:
                bowlers_runs_in_2015[bowler] = {"run": runs, "balls": 1}


    return bowlers_runs_in_2015


def plot(bowlers_runs_in_2015):

        bowlers_economy = {}

        # print(bowlers_runs_in_2015)

        for bowler in bowlers_runs_in_2015:

            total_balls = bowlers_runs_in_2015[bowler]["balls"]
            total_run = bowlers_runs_in_2015[bowler]["run"]

            overs = total_balls/6
            eco = total_run/overs

            bowlers_economy[bowler] = round(eco,2)


        final_dict=dict(sorted(bowlers_economy.items(),key=lambda x : x[1])[:10])

        x_axis = final_dict.keys()
        y_axis = final_dict.values()


        plt.figure(figsize=(10,10))
        plt.xlabel("Bowlers names")
        plt.ylabel("Economy")
        plt.title("Top 10 economical bowlers of 2015")
        plt.xticks(rotation=90)

        bars=plt.bar(x_axis,y_axis)

        plt.bar_label(bars)

        plt.tight_layout()

        plt.savefig(output_images_path/"q8_top10_economical_bowler_in_2015.png")
        plt.show()


def execute(matches_list,deliveries_list):
    bowlers_runs_in_2015 = calculate(matches_list,deliveries_list)
    plot(bowlers_runs_in_2015)

    return bowlers_runs_in_2015

execute(matches_list,deliveries_list)