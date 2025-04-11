import random
secret_number = str(random.randint(1000, 9999))
attempts = 0
print("\nI have generated four digit number with unique digit.Try to guess it.")

while True:
    guess = input("Guess: ")
    if len(guess) != 4 or not guess.isdigit():
        print("Invalid guess! Please enter a 4-digit number.")
        continue
    attempts += 1
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret_number[i]:
            bulls += 1
    for i in range(4):
        if guess[i] != secret_number[i] and guess[i] in secret_number:
            cows += 1
    print(f"{bulls} bulls, {cows} cows.")
    if bulls == 4:
        print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts.")
        break
