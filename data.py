import csv
import os
import kagglehub

from pathlib import Path


#No need to run it, This file will be executed by python automatically when variable be imported in another file.
#This file contains data information.Used this technique to separate data and logic.


path = kagglehub.dataset_download("manasgarg/ipl")
    #this return path where datasets are downloaded in ur local machine.
    # path --> /Users/raghvendra/.cache/kagglehub/datasets/manasgarg/ipl/versions/1

    # In this path 2 csv files will be present matches.csv , deliveries.csv

all_dir = os.listdir(path)
    # os.listdir() returns all files/folders inside the path as a list.
    #will export all_dir to other files.

output_images_path = Path(__file__).parent / "output_images"

matches_url = path + "/" + all_dir[0]
deliveries_url = path + "/" + all_dir[1]


def matches_info(matches_url):

    with open(matches_url,"r") as file:
        matches_data = list(csv.DictReader(file))

        return matches_data


def deliveries_info(deliveries_url):

    with open(deliveries_url,"r") as file:
        deliveries_data = list(csv.DictReader(file))

        return deliveries_data


matches_list = matches_info(matches_url)
deliveries_list = deliveries_info(deliveries_url)









