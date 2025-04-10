import random

while True:
    x = random.randint(1, 100)
    user_input = int(input("Guess the number between 1 and 100: "))
    while user_input != x:
        if user_input < x:
            print("Too low")
        elif user_input > x:
            print("Too high")

        user_input = int(input("Guess again: "))

    print("You got it!")
    new_guess = input("Would you like to play again? (y/n): ")
    if new_guess.lower() == "n":
        break
