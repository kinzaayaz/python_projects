import random
while True:
    num1,num2=random.randint(1,6),random.randint(1,6)
    print(f'({num1},{num2})')
    play_again=input("Roll the dice? (y/n): ").lower()
    if play_again=="n":
        break
    
