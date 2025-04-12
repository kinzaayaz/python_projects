import random
player1_score=0
player2_score=0
while player1_score<100 and player2_score<100:
    turn_score=0
    print("Player 1's turn.")
    while True:
        roll= random.randint(1,6)
        print(f"You roll {roll}")
        turn_score+=roll
        if roll==1:
            print("You roll 1.you lost all points")
            break
        Choice=input("Roll again?(y/n): ").lower()
        if Choice=="n":
            break
    player1_score+=turn_score
    print(f"Current scores: Player 1: {player1_score}, Player 2: {player2_score}")

    if player1_score >= 100:
        print("\n Player 1 wins!")
        break
    
    print("\n Player 2's turn.")
    while True:
        roll= random.randint(1,6)
        print(f"You roll {roll}")
        turn_score+=roll
        if roll==1:
            print("You roll 1.you lost all points")
            break
        Choice=input("Roll again?(y/n): ").lower()
        if Choice=="n":
            break
    player2_score+=turn_score
    print(f"Current scores: Player 1: {player1_score}, Player 2: {player2_score}")

    if player2_score >= 100:
        print("\n Player 2 wins!")
    break
    

        
        