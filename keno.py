# Keno
# Function accepts a list of numbers that the player wants to bet on.
# They also select their bet.
import random
# Choose how much money you put in the machine
wallet = 10
# Might only allow integers as bets for now, but decimal would be alright
bet = 1
# Player puts in a comma separated set of numbers in the player_picks variable.
player_picks = [3, 4, 5, 50, 57, 11, 31]
def play(lst, bet, wallet):
    if wallet < bet:
        "Please input more coins."
    if len(player_picks) == 0 or len(player_picks) > 10:
        "Please select a spot between one and ten numbers."
# Sample method produces a non repeating list of integers
    smp = random.sample(range(1,100),10)
    match = []
    win = 0
    wallet = wallet - bet
    for i in lst:
        if i in smp:
            match.append(i)
    if len(match) < 3:
        print(win)
    elif len(match) == 3:
        win += 3 * bet
    elif len(match) == 4:
        win += 4 * bet
    elif len(match) == 5:
        win += 10 * bet
    elif len(match) == 6:
        win += 50 * bet
    elif len(match) == 7:
        win += 100 * bet
    elif len(match) == 8:
        win += 250 * bet
    elif len(match) == 9:
        win += 500 * bet
    elif len(match) == 10:
        win += 1000 * bet
    print("You bet $" + str(bet) + "\n"
          "On the following spot: " + str(lst) + "\n"
          "The machine drew these numbers: " + str(smp) + "\n"
          "You matched " + str(len(match)) + " numbers, which are" + str(match) + "\n"
          "You won $" + str(win) + " and now have $" + str(wallet))
play(player_picks, bet, wallet)
