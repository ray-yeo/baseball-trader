import csv

#STEP 1: run the correct python file depending on pitcher or batter

while True:
    trade_type = input("Enter 'B' if trading Position Players. Enter 'P' if trading Starting Pitchers. ")
    if trade_type == "B":
        data = open("batters_stats.csv", encoding = "utf-8")
        break
    elif trade_type == "P":
        data = open("pitchers_stats.csv", encoding = "utf-8")
        break

csv_data = csv.reader(data)
data_lines = list(csv_data)

# Batters
#['', 'PLAYER', 'YRS', 'G', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'BB', 'SO', 'SB', 'CS', 'BA']

#Pitchers
#['', 'PLAYER', 'YRS', 'G', 'GS', 'CG', 'SH', 'IP', 'H', 'ER', 'BB', 'SO', 'W', 'L', 'SV', 'ERA']


#STEP 2: find player one's statistics + compute

found = False
while not found:
    player_one = input("Enter Player 1's name: ").lower()
    print("Finding and crunching Player 1's stats...")
    #STEP 2: find player one's statistics + compute
    for i in range(1,len(data_lines)):
        if data_lines[i][1] == player_one:
            player_one_data = data_lines[i]
            found = True
            break
    if found == False:
        print("Could not find that player. Please re-enter the player's name.")


print("Successfully obtained Player 1's data")

if trade_type == "B":
    rbis = float(player_one_data[10])
    runs = float(player_one_data[5])
    hrs = float(player_one_data[9])
    player_one_strength = (0.5 * rbis) + (0.2 * runs) + (hrs)
else:
    era = float(player_one_data[15])
    strikeouts = float(player_one_data[11])
    walks = float(player_one_data[10])
    player_one_strength = (80 - 10 * era) + (0.2 * strikeouts) - (0.1 * walks)

#STEP 3: find player two's statistics + compute


found = False
while not found:
    player_two = input("Enter Player 2's name: ").lower()
    print("Finding and crunching Player 2's stats...")
    for i in range(1,len(data_lines)):
        if data_lines[i][1] == player_two:
            player_two_data = data_lines[i]
            found = True
            break
    if found == False:
        print("Could not find that player. Please re-enter the player's name.")

if trade_type == "B":
    rbis = float(player_two_data[10])
    runs = float(player_two_data[5])
    hrs = float(player_two_data[9])
    player_two_strength = (0.5 * rbis) + (0.2 * runs) + (hrs)
else:
    era = float(player_two_data[15])
    strikeouts = float(player_two_data[11])
    walks = float(player_two_data[10])
    player_two_strength = (80 - 10 * era) + (0.2 * strikeouts) - (0.1 * walks)

#compare the players

print(player_one + " has a computed strength of " + str(player_one_strength))
print(player_two + " has a computed strength of " + str(player_two_strength))

if abs(player_one_strength-player_two_strength) < 10:
    print("this is a pretty fair trade")

elif abs(player_one_strength-player_two_strength) > 10 and player_one_strength>player_two_strength:
    print("this is an unfair trade. " + player_one + " has had a better season." )

elif abs(player_one_strength-player_two_strength) > 10 and player_one_strength < player_two_strength:
    print("this is an unfair trade. " + player_two + " has had a better season." )
