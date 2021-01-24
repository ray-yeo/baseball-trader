import csv
import time

for i in range(40):
    print("")

print("Welcome to my baseball trade analyzer!")
time.sleep(2)
print("")

print("When prompted, choose the type of players you are trading.")
time.sleep(2)
print("")

print("Please note that at the moment you may only trade hitters with hitters, and pitchers with pitchers.")
time.sleep(2)
print("")

print("Additionally, you may only trade players who played a full season in 2019.")
time.sleep(2)
print("")


#STEP 1: run the correct python file depending on pitcher or batter

while True:
    trade_type = input("Enter 'B' if trading Position Players. Enter 'P' if trading Starting Pitchers. Enter 'Q' if you like to quit. ")
    if trade_type == "B":
        data = open("batters_stats.csv", encoding = "utf-8")
        break
    elif trade_type == "P":
        data = open("pitchers_stats.csv", encoding = "utf-8")
        break
    elif trade_type == "Q":
        print("")
        time.sleep(0.5)
        print("See you next time!")
        print("")
        quit()

print("")
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
    print("Finding and crunching {} stats...".format(player_one))
    time.sleep(1)
    print("")
    #STEP 2: find player one's statistics + compute
    for i in range(1,len(data_lines)):
        if data_lines[i][1] == player_one:
            player_one_data = data_lines[i]
            found = True
            break
    if found == False:
        print("Could not find that player. Please re-enter the player's name.")
        print("")


print("Here is {}'s statline".format(player_one))
print(data_lines[0][3:])
print(player_one_data[3:])
print("")

if trade_type == "B":
    avg = min(((float(player_one_data[15]) * 1000 / 2) - 65), 100)
    rbis = min(float(player_one_data[10]), 100)
    hrs = min(float(player_one_data[9])*2, 100)
    runs = min(float(player_one_data[5])-20, 100)
    player_one_strength = round((avg + rbis + hrs + runs)/4 , 2)
else:
    era = (10 - float(player_one_data[15])) * 13.33333
    innings = (float(player_one_data[7]) - 15) / 2
    wins = float(player_one_data[12]) * 5
    player_one_strength = round((era + innings + wins) / 3 , 2)

#STEP 3: find player two's statistics + compute


found = False
while not found:
    player_two = input("Enter Player 2's name: ").lower()
    print("Finding and crunching {} stats...".format(player_two))
    time.sleep(1)
    print("")
    for i in range(1,len(data_lines)):
        if data_lines[i][1] == player_two:
            player_two_data = data_lines[i]
            found = True
            break
    if found == False:
        print("Could not find that player. Please re-enter the player's name.")
        print("")


print("Here is {}'s statline".format(player_two))
print(data_lines[0][3:])
print(player_two_data[3:])
print("")

if trade_type == "B":
    avg = min(((float(player_two_data[15]) * 1000 / 2) - 65), 100)
    rbis = min(float(player_two_data[10]), 100)
    hrs = min(float(player_two_data[9])*2, 100)
    runs = min(float(player_two_data[5])-20, 100)
    player_two_strength = round((avg + rbis + hrs + runs) / 4 , 2)
else:
    era = (10 - float(player_two_data[15])) * 13.33333
    innings = (float(player_two_data[7]) - 15) / 2
    wins = float(player_two_data[12]) * 5
    player_two_strength = round((era + innings + wins) / 3 , 2)
#compare the players

time.sleep(1)


print(player_one + " has a computed strength of " + str(player_one_strength))
print("")
print(player_two + " has a computed strength of " + str(player_two_strength))

time.sleep(1)
print("")

if abs(player_one_strength-player_two_strength) <= 10:
    print("this is a pretty fair trade")

elif abs(player_one_strength-player_two_strength) > 10 and player_one_strength>player_two_strength:
    print("this is an unfair trade. " + player_one + " has had a better season." )

elif abs(player_one_strength-player_two_strength) > 10 and player_one_strength < player_two_strength:
    print("this is an unfair trade. " + player_two + " has had a better season." )

print("")
