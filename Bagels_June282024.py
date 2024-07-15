from tabulate import tabulate
from random import randint

def generate_num():
    num = str(randint(0, 10))
    if len(num) < 3:
        num = list(num)
        if len(num) < 2:
            num.insert(0, "00")
        else:
            num.insert(0, "0")
        num = ''.join(num)
    return num


def check_guess(user, computer):
    count = []
    for i in range(len(computer)):
        if user[i] in computer:
            if user[i] == computer[i]:
                count.append("Fermi")
            else:
                count.append("Pico")
    if len(count) == 0:
        print("Bagels")
    else:
        count.sort()
        print(' '.join(count))

def game():
    data = [["Pico", "One digit is correct but in the wrong position."], ["Fermi", "One digit is correct and in the right position."], 
            ["Bagels", " No digit is correct."]]

    col_names = ["When I say:", "That means:"]

    guesses = 10

    print("Bagels, a deductive logic game.")
    print("By Al Sweigart al@inventwithpython.com")
    print("I am thinking of a 3-digit number. Try to guess what it is.")
    print("Here are some clues:")
    print(tabulate(data, headers=col_names, tablefmt="grid"))
    print("I have thought up a number.")

    answer = generate_num()
    game_on = True
    while game_on:
        print(answer)
        print(f"You have {guesses} guesses left to get it.")
        user_guess = input("Guess the number: ")
        if user_guess != answer:
            check_guess(user_guess, answer)
            guesses -= 1  
        if user_guess == answer:
            game_on = False
            print("You got it!")
        elif guesses == 0:
            game_on = False
            print(f"You've ran out of guesses. Game over. The answer is {answer}.")
    
    if input("Do you want to continue playing? ").lower().startswith("y"):
        game()

game()