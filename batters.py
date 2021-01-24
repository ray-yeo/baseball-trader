import pandas as pd
import re
import requests
import bs4

#50 results per page
for i in range(1, 346, 50):

    #page 1
    url = "http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2019/start/{}".format(i)
    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.text, "html.parser")

    header = soup.find("tr", attrs= {"class": "colhead"})
    columns = [col.get_text() for col in header.find_all("td")]

    if i==1:
        final_df = pd.DataFrame(columns = columns)

    players = soup.find_all('tr', attrs={'class':re.compile('row player-10-')})

    for player in players:
        stats = [stat.get_text() for stat in player.find_all("td")]
        #lowercase the names
        stats[1] = stats[1].lower()
        temp_df = pd.DataFrame(stats).transpose()
        temp_df.columns = columns
        final_df = pd.concat([final_df, temp_df], ignore_index = True)

final_df.to_csv(r"batters_stats.csv", index = False, sep = ',', encoding = "utf-8")
