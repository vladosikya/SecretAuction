from logo import gavel
import os

game_base = {}
auction = True

while auction:
    print(gavel)
    name = input("What is your name? ")

    while True:
        try:
            bet = input("What is your bet size? $")
            int(bet)
            break
        except:
            print("Need number")


    game_base[name] = bet
    while True:
        repeat = input("Will other players still bet? 'yes' or 'no' ")
        if repeat == "yes":
            os.system('cls||clear')
            print(100 * '\n')
            break
        elif repeat == "no":
            auction = False
            break
        else:
            print("Unknown command.")

bet_winnder = 0
chara_winner = ""

for chara in game_base:
    bet = int(game_base[chara])
    if bet > bet_winnder:
        bet_winnder = bet
        chara_winner = chara

print(f"{chara_winner} won with a bet of ${bet_winnder}.")

