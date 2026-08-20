import matplotlib.pyplot as plt
from data import matches_list
from data import output_images_path


#My logic---> Teams --> seasons--->Number of matches.

def calculate(matches_list):

    team_matches_per_season = {}

    for match in matches_list:
        team = match["team1"]
        season = match["season"]

        if(team in team_matches_per_season.keys()):    #if team exist in team list

            if(season in team_matches_per_season[team].keys()): #If season exist in team's season.
                team_matches_per_season[team][season] += 1
            else:
                team_matches_per_season[team][season] = 1
        else:
                team_matches_per_season[team] = {season:1}

    return team_matches_per_season


def plot(team_matches_per_season):

    bottom = [0] * len(team_matches_per_season)

    years = []

    # Get all seasons
    for team in team_matches_per_season:
        for season in team_matches_per_season[team].keys():
            years.append(season)

    # Remove duplicates and sort
    years = sorted(set(years))

    teams = list(team_matches_per_season.keys())

    # Process one year at a time
    for year in years:

        values = []

        # Get games for every team for this year
        for team in teams:

            if year in team_matches_per_season[team].keys():
                val = team_matches_per_season[team][year]
            else:
                val = 0

            values.append(val)

        # Draw this year's bars in graph on top of previous bar graph.
        #bottom is doing the magic.
        plt.bar(
            teams,
            values,
            bottom=bottom,
            label=year
        )

        # Update bottom
        for i in range(len(values)):
            bottom[i] += values[i] 



    plt.xticks(rotation=90)     #out of loop plotting graph
    plt.xlabel("Team")
    plt.ylabel("Number of Games")
    plt.title("Number of Games per Season of every team")

    plt.legend(     #this is the for box of colour representing season
        title="Season",
        bbox_to_anchor=(1.0, 1),
        loc="upper left"
    )



    plt.tight_layout()

    plt.savefig(output_images_path/"q4_number_of_games_played_by_team_in_each_season.png")
    plt.show()


def execute(matches_list):
    team_matches_per_season = calculate(matches_list)
    plot(team_matches_per_season)

    return team_matches_per_season

execute(matches_list)