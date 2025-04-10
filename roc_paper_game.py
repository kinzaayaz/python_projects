import random

while True:
    user_choice = input("rock, paper, scissors? (r/p/s): ").lower()
    if user_choice not in ['r', 'p', 's']:
        print("Invalid choice! Please choose 'r' for rock, 'p' for paper, or 's' for scissors.")
        continue
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print("You chose: ", user_choice)
    print("Computer chose: ", computer_choice)
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 'r':
        if computer_choice == 'paper':
            print("Computer wins!")
        else:
            print("You win!")
    elif user_choice == 'p':
        if computer_choice == 'scissors':
            print("Computer wins!")
        else:
            print("You win!")
    elif user_choice == 's':
        if computer_choice == 'rock':
            print("Computer wins!")
        else:
            print("You win!")
    
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == 'n':
        print("Goodbye!")
        break