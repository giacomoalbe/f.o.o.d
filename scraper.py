from bs4 import BeautifulSoup

import requests
import csv

def add_result(row, data, csv_writer):
    columns = row.find_all("td")

    ora = columns[1].text
    team1 = columns[2].find("a").text
    team2 = columns[4].find("a").text

    # 3:2
    raw_match_result = columns[5].find("a").text.split(" ")[0]

    team_1_goals =  raw_match_result.split(":")[0]
    team_2_goals =  raw_match_result.split(":")[1]

    if team_1_goals > team_2_goals:
        match_result = "1"
    elif team_1_goals < team_2_goals:
        match_result = "2"
    else:
        match_result = "X"

    csv_writer.writerow([data, team1, team2, team_1_goals, team_2_goals, match_result])

    print("[{0} {1}] {2:20} - {4:>20} ({3}:{5}) R: {6}".format(data, ora, team1, team_1_goals, team2, team_2_goals, match_result))

def get_results_from_year(year, csv_writer):
    print("Inizio richiesta...")
    url_formatted = url.format(year, year + 1)

    request = requests.get(url_formatted)

    soup = BeautifulSoup(request.text, 'html.parser')

    table_results = soup.find(class_="portfolio").find(class_="box").find("table").find_all("tr")

    row_counter = 0
    match_date = ""

    for row in table_results:
        # tr with th inside does not contain any data
        if row.find("th") == None:
            row_counter += 1

            if row.find("td").text != "":
                match_date = row.find("td").text

            add_result(row, match_date, csv_writer)

    print("Results row number: {}".format(row_counter))

url = "http://www.calcio.com/tutte_le_partite/ita-serie-a-{}-{}/"

with open('results/match_results.csv', mode='w') as csv_result:
    csv_result_writer = csv.writer(csv_result, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    csv_result_writer.writerow(["Data", "Team 1", "Team 2", "Goal Team 1", "Goal Team 2", "Match Result"])

    for year in range(2015, 2020):
        get_results_from_year(year, csv_result_writer)
