import matplotlib.pyplot as plt
from data import matches_list
from data import output_images_path


def calculate(matches_list):

    umpires_list = {}

    for match in matches_list:
        umpire1 = match["umpire1"]
        umpire2 = match["umpire2"]
        umpire3 = match["umpire3"]

        if(umpire1 != "NaN" and (umpire1 not in umpires_list)):
            umpires_list[umpire1] = "NA"

        if (umpire2 != "NaN" and (umpire2 not in umpires_list)):
            umpires_list[umpire2] = "NA"

        if (umpire3 != "NaN" and (umpire3 not in umpires_list)):
            umpires_list[umpire3] = "NA"


    #After filling umpires_list, I used some source to get their respected country.

    umpires_country = {
        "AY Dandekar": "India",
        "NJ Llong": "England",
        "": "NA",
        "A Nand Kishore": "India",
        "S Ravi": "India",
        "Nitin Menon": "India",
        "CK Nandan": "India",
        "AK Chaudhary": "India",
        "C Shamshuddin": "India",
        "A Deshmukh": "India",
        "KN Ananthapadmanabhan": "India",
        "YC Barde": "India",
        "VK Sharma": "India",
        "CB Gaffaney": "New Zealand",
        "M Erasmus": "South Africa",
        "Asad Rauf": "Pakistan",
        "RE Koertzen": "South Africa",
        "MR Benson": "England",
        "SL Shastri": "India",
        "Aleem Dar": "Pakistan",
        "GA Pratapkumar": "India",
        "SJ Davis": "Australia",
        "DJ Harper": "Australia",
        "BF Bowden": "New Zealand",
        "K Hariharan": "India",
        "RB Tiffin": "Zimbabwe",
        "IL Howell": "South Africa",
        "AM Saheba": "India",
        "AV Jayaprakash": "India",
        "I Shivram": "India",
        "BR Doctrove": "West Indies",
        "BG Jerling": "South Africa",
        "SD Ranade": "India",
        "SJA Taufel": "Australia",
        "TH Wijewardene": "Sri Lanka",
        "HDPK Dharmasena": "Sri Lanka",
        "S Asnani": "India",
        "GAV Baxter": "Australia",
        "SK Tarapore": "India",
        "SS Hazare": "India",
        "S Das": "India",
        "PR Reiffel": "Australia",
        "AL Hill": "New Zealand",
        "RJ Tucker": "Australia",
        "JD Cloete": "South Africa",
        "VA Kulkarni": "India",
        "BNJ Oxenford": "Australia",
        "K Srinath": "India",
        "Subroto Das": "India",
        "RK Illingworth": "England",
        "RM Deshpande": "India",
        "PG Pathak": "India",
        "SD Fry": "Australia",
        "K Srinivasan": "India",
        "K Bharatan": "India"
    }

    country_and_umpires_count={}

    for country in umpires_country.values():

        if country == "India":
            continue

        if(country in country_and_umpires_count):
            country_and_umpires_count[country] += 1
        else:
            country_and_umpires_count[country] = 1

    return country_and_umpires_count


def plot(country_and_umpires_count):

    plt.figure(figsize=(10,10))
    plt.xlabel("Country")
    plt.ylabel("Umpires count")
    plt.title("Total number of umpires from each Country")
    plt.xticks(rotation=90)

    bars = plt.bar(country_and_umpires_count.keys(), country_and_umpires_count.values())
    plt.bar_label(bars)


    plt.tight_layout()
    plt.savefig(output_images_path/"q3_umpires_origin_in_ipl.png")
    plt.show()



def execute(matches_list):
    country_and_umpires_count=calculate(matches_list)
    plot(country_and_umpires_count)

    return country_and_umpires_count


execute(matches_list)


