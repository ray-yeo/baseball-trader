Inspiration

I decided to built this application because I'm really into baseball statistics, and I want to get better at fantasy baseball. Thus, I built this trade analyzer so I could evaluate transactions for this upcoming season.

What it does

The entire application is made up of three files. The first two files web scrape a historical statistics page on ESPN, and puts the information into a CSV file for easy access. The third file is what is actually run in the terminal. This searches for the inputted players in the CSV files, obtains relevant stats, computes a "strength index" for each player, and compares to two to see if the trade is "fair".

How I built it

I was able to get a lot of web scraping guidance from the following article: https://news.codecademy.com/web-scraping-python-beautiful-soup-mlb-stats/. After getting all the necessary data, I had to figure out how to weight each statistical category. What I settled on was determining what a "perfect" stat would look like, and assigning it 100 points. For example, I decided that a perfect batting average would be 0.330, and anything above that would earn a player 100 points to their strength index. A similar process followed for other categories as well, and a player's final strength score was an average of all of these. The "fairness" of a trade was determined by whether the strength scores of two players were within 10.

Challenges I ran into

Finding a proper website: There are a lot of baseball statistics websites out there, so I had difficulty settling on one. While the more advanced ones were great, they were much more difficult to parse through. Thus, I settled on the most basic ESPN stats website so that I could get my project started ASAP.
Calculating strength scores: It was tough coming up with a logical way to score each player. I started off by assigning random weights to random categories, just to see how it would work out. However, this led to very inaccurate results. That's when I remembered about a super cool baseball statistic called "WAR". In short, WAR compares each player to an "average player", and assigns a player's value based on that. I decided to take a similar route in my weighting system, but by comparing each player to a "perfect player" with a score of 100.

What's next

Baseball is all about trends, and my program only takes 2019 stats into account. A more accurate measure would be to take a weighted sum of a player's most recent stats, as well as career average stats (potentially in a 60/40 split)
I also want to make it possible to trade multiple players, which is more representative of how trades work in baseball. Additionally, I want to make trading between batters and pitchers possible.
Another cool addition would be to web scrape a more advanced website so I can obtain more "interesting" data points (like OBP, OPS, WHIP, FIP, WAR, etc.)