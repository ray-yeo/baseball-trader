import pandas as pd
import re
import requests
import bs4

#page 1
url = "http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2019/start/1"
page = requests.get(url)
soup = bs4.BeautifulSoup(page.text, "html.parser")

header = soup.find("tr", attrs= {"class": "colhead"})
columns = [col.get_text() for col in header.find_all("td")]

final_df = pd.DataFrame(columns = columns)

players = soup.find_all('tr', attrs={'class':re.compile('row player-10-')})

for player in players:
    stats = [stat.get_text() for stat in player.find_all("td")]
    #lowercase the names
    stats[1] = stats[1].lower()
    temp_df = pd.DataFrame(stats).transpose()
    temp_df.columns = columns
    final_df = pd.concat([final_df, temp_df], ignore_index = True)

#page 2
url = "http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2019/start/51"
page = requests.get(url)
soup = bs4.BeautifulSoup(page.text, "html.parser")

header = soup.find("tr", attrs= {"class": "colhead"})
columns = [col.get_text() for col in header.find_all("td")]

players = soup.find_all('tr', attrs={'class':re.compile('row player-10-')})

for player in players:
    stats = [stat.get_text() for stat in player.find_all("td")]
    #lowercase the names
    stats[1] = stats[1].lower()
    temp_df = pd.DataFrame(stats).transpose()
    temp_df.columns = columns
    final_df = pd.concat([final_df, temp_df], ignore_index = True)

#page 3
url = "http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2019/start/101"
page = requests.get(url)
soup = bs4.BeautifulSoup(page.text, "html.parser")

header = soup.find("tr", attrs= {"class": "colhead"})
columns = [col.get_text() for col in header.find_all("td")]

players = soup.find_all('tr', attrs={'class':re.compile('row player-10-')})

for player in players:
    stats = [stat.get_text() for stat in player.find_all("td")]
    #lowercase the names
    stats[1] = stats[1].lower()
    temp_df = pd.DataFrame(stats).transpose()
    temp_df.columns = columns
    final_df = pd.concat([final_df, temp_df], ignore_index = True)


#page 4
url = "http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2019/start/151"
page = requests.get(url)
soup = bs4.BeautifulSoup(page.text, "html.parser")

header = soup.find("tr", attrs= {"class": "colhead"})
columns = [col.get_text() for col in header.find_all("td")]

players = soup.find_all('tr', attrs={'class':re.compile('row player-10-')})

for player in players:
    stats = [stat.get_text() for stat in player.find_all("td")]
    #lowercase the names
    stats[1] = stats[1].lower()
    temp_df = pd.DataFrame(stats).transpose()
    temp_df.columns = columns
    final_df = pd.concat([final_df, temp_df], ignore_index = True)


#page 5
url = "http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2019/start/201"
page = requests.get(url)
soup = bs4.BeautifulSoup(page.text, "html.parser")

header = soup.find("tr", attrs= {"class": "colhead"})
columns = [col.get_text() for col in header.find_all("td")]

players = soup.find_all('tr', attrs={'class':re.compile('row player-10-')})

for player in players:
    stats = [stat.get_text() for stat in player.find_all("td")]
    #lowercase the names
    stats[1] = stats[1].lower()
    temp_df = pd.DataFrame(stats).transpose()
    temp_df.columns = columns
    final_df = pd.concat([final_df, temp_df], ignore_index = True)


#page 6
url = "http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2019/start/251"
page = requests.get(url)
soup = bs4.BeautifulSoup(page.text, "html.parser")

header = soup.find("tr", attrs= {"class": "colhead"})
columns = [col.get_text() for col in header.find_all("td")]

players = soup.find_all('tr', attrs={'class':re.compile('row player-10-')})

for player in players:
    stats = [stat.get_text() for stat in player.find_all("td")]
    #lowercase the names
    stats[1] = stats[1].lower()
    temp_df = pd.DataFrame(stats).transpose()
    temp_df.columns = columns
    final_df = pd.concat([final_df, temp_df], ignore_index = True)


#page 7
url = "http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2019/start/301"
page = requests.get(url)
soup = bs4.BeautifulSoup(page.text, "html.parser")

header = soup.find("tr", attrs= {"class": "colhead"})
columns = [col.get_text() for col in header.find_all("td")]

players = soup.find_all('tr', attrs={'class':re.compile('row player-10-')})

for player in players:
    stats = [stat.get_text() for stat in player.find_all("td")]
    #lowercase the names
    stats[1] = stats[1].lower()
    temp_df = pd.DataFrame(stats).transpose()
    temp_df.columns = columns
    final_df = pd.concat([final_df, temp_df], ignore_index = True)


final_df.to_csv(r"batters_stats.csv", index = False, sep = ',', encoding = "utf-8")
