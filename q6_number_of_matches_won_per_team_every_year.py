import matplotlib.pyplot as plt
from data import matches_list
from data import output_images_path




def calculate(matches_list):
    team_seasons_wins_count = {}

    for match in matches_list:
        year = str(match["season"])
        winnerTeam = str(match["winner"])

        if (winnerTeam in team_seasons_wins_count.keys()):

            if (year in team_seasons_wins_count[winnerTeam].keys()):
                team_seasons_wins_count[winnerTeam][year] += 1
            else:
                team_seasons_wins_count[winnerTeam][year] = 1
        else:
            team_seasons_wins_count[winnerTeam] = {year: 1}


    return team_seasons_wins_count




def plot(team_seasons_wins_count):

    plt.figure(figsize=(10,10)) #Graph layout size.

    all_years = []

    for team in team_seasons_wins_count:
        for year in team_seasons_wins_count[team].keys():
            all_years.append(year)

    all_years = sorted(set(all_years))
    all_teams = list(team_seasons_wins_count.keys())

    bottom = [0] * len(all_teams)

    for year in all_years:

        every_team_current_year_won_count = []
        for team in team_seasons_wins_count.keys():
            won_matches = 0

            if(year in team_seasons_wins_count[team].keys()):
                won_matches = team_seasons_wins_count[team][year]
            every_team_current_year_won_count.append(won_matches)

        plt.bar(all_teams,every_team_current_year_won_count,bottom=bottom,label=year)

        new_bottom = [0]*len(bottom)

        for i in range(len(bottom)):
            new_bottom[i] = bottom[i] + every_team_current_year_won_count[i]

        bottom = new_bottom



    #plotting
    plt.xlabel("Teams")
    plt.legend()
    plt.ylabel("Won matches each season")
    plt.title("Number of matches won by teams every year")
    plt.xticks(all_teams,rotation=90)
    plt.tight_layout()
    plt.savefig(output_images_path/"q6_number_of_matches_won_per_team_every_year.png")
    plt.show()





def execute(matches_list):
    team_seasons_wins_count = calculate(matches_list)
    plot(team_seasons_wins_count)

    return team_seasons_wins_count

execute(matches_list)