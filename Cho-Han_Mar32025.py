from random import randint
import time
import sys

def dice_roll():
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    return (dice1, dice2)

def check_win(dice1, dice2, chohan):
    return (chohan == "CHO" and (dice1 + dice2) % 2 == 0) or (chohan == "HAN" and (dice1 + dice2) % 2 != 0)

def bet_money(money):
    while True:
        bet = input(f"You have {money} mon. How much do you bet? (or QUIT)").upper()
        if bet == "QUIT":
            sys.exit()
        elif int(bet) > money:
            print("You do not have enough money to make that bet.")
        else:
            bet = int(bet)
            break
    return bet

def specific_number():
    while True:
        choice = input("Do you want to bet on a specific number? Bonus or loss of 20 mon if you win, or lose.").lower()
        if choice not in ["y", "yes", "n", "no"]:
            print("Please answer with a 'y' or 'n'.")
        else:
            if choice.startswith("y"):
                num = input("Pick your number/s.").split()
                return num
            else:
                return


def Cho_Han():    
    JAPANESE_NUMBERS = {1: "ichi", 2: "ni", 3: "san", 4: "yon", 5: "go", 6: "roku"}
    
    money = 5000
    game_on = True

    while game_on:
        print("Cho-Han, by Al Sweigart al@inventwithpython.com")
        print("""In this traditional Japanese dice game, two dice are rolled in a bamboo cup by the dealer sitting on the floor. The player must guess if the dice total to an even (cho) or odd (han) number.""")
        bet = bet_money(money)
        winnings = bet*2
        dice1, dice2 = dice_roll()
        print(dice1, dice2)
        number = specific_number()
        print(number)
        chohan = input("""The dealer swirls the cup and you hear the rattle of dice. The dealer slams the cup on the floor, still covering the dice and asks for your bet. CHO (even) or HAN (odd)?""").upper()
        print(f"The dealer lifts the cup to reveal:")
        time.sleep(1)
        print(f"{JAPANESE_NUMBERS[dice1]} - {JAPANESE_NUMBERS[dice2]}")
        print(F"{dice1} - {dice2}")
        if check_win(dice1, dice2, chohan):
            print(f"You won! You take {winnings} mon.")
            money += winnings
        else:
            print(f"You lost. ")
            money -= bet
        if number:
            if  len(number) == 2 and ((number[0] == str(dice1) and number[1] == str(dice2)) or (number[0] == str(dice2) and number[1] == str(dice2))):
                print("You won an additional 40 mon for guessing the correct number in both dice.")
                money += 40
            elif len(number) == 2 and (number[0] == str(dice1) or number[0] == str(dice2) or number[1] == str(dice1) or number[1] == str(dice2)):
                print("You won an additional 20 mon for guessing the correct number in one dice.")
                money += 20
            elif len(number) == 1 and (number[0] == str(dice1) or number[0] == str(dice2)):
                print("You won an additional 20 mon for guessing the correct number in one dice.")
                money += 20
            else:
                print("You lost 40 mon.")
                money -= 40
        house_fee = bet // 10
        print(f"The house collects a {house_fee} mon fee.")
        money -= house_fee
        if money <= 0:
            print('You have run out of money!')
            print('Thanks for playing!')
            sys.exit()

Cho_Han()
