import random

while True:
    symbols = ['🍒', '🍋', '🍉']
    balance = int(input("Enter starting balance: "))
    print("Welcome to the Slot Machine Game!")
    print("You start with balance of", balance)
    
    while balance>0:
        print("Current balance: ", balance)
        bet_amount=int(input("Enter bet amount: "))    
        if bet_amount==0:
            print(f"Thanks for playing! You walked away with ${balance}.")
            break     
        if bet_amount>balance:
            print("Bet amount exceeds current balance.")
            continue
        
        spin=random.choices(symbols, k=3)
        print("|",spin[0],"|", spin[1],"|", spin[2],"|")
 
        if spin[0] == spin[1] == spin[2]:
            winning_amount = bet_amount * 10
            print(f"You won ${winning_amount}!")
        elif spin[0]==spin[1] or spin[1]==spin[2] or spin[0]==spin[2]:
            winning_amount = bet_amount * 2
            print(f"You won ${winning_amount}!")
            balance += winning_amount
        else:
            balance-=bet_amount
            print(f"You lost ${bet_amount}.")
        

        if balance <= 0:
            print("You ran out of money! Game over!")
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break
