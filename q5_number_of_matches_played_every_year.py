import matplotlib.pyplot as plt

from data import matches_list
from data import output_images_path


def calculate(matches_list):

    total_matches_every_year = {}

    for match in matches_list:
        year = match["season"]

        if year in total_matches_every_year.keys():
            total_matches_every_year[year] += 1
        else:
            total_matches_every_year[year] = 1


    return total_matches_every_year



def plot(total_matches_every_year):

    plt.figure(figsize=(10,10))

    bars=plt.bar(total_matches_every_year.keys(),total_matches_every_year.values(),width=0.5)

    plt.xlabel('Years')
    plt.ylabel('Number of Matches')
    plt.title("Total Number of matches played every year")

    plt.bar_label(bars)     #It needs object returned by plt.bar()
                            # that object looks like Array of arrayofkeys and arrayofvals.

    plt.savefig(output_images_path/"q5_number_of_matches_played_every_year.png")
    plt.show()






def execute(matches_list):
    total_matches_every_year = calculate(matches_list)
    plot(total_matches_every_year)

    return total_matches_every_year


execute(matches_list)