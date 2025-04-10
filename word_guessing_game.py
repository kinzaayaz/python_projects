import random
words = ["star", "hello", "python", "world", "rose"]
word = random.choice(words)
guesses = ""  
turns = 6 

word_display = "_ " * len(word)
print(word_display)

while turns > 0:
    user_input = input("\nEnter a letter: ").lower()  
    if len(user_input) != 1 or not user_input.isalpha():
        print("Please enter only one letter.")
        continue
    
    if user_input in guesses:
        print(f"You already guessed '{user_input}'. Try a different letter.")
        continue
    
    if user_input in word:
        guesses += user_input
        print("Correct guess!")
    else:
        turns -= 1
        print("Wrong guess!")
    
    word_display = ""
    for letter in word:
        if letter in guesses:
            word_display += letter + " "
        else:
            word_display += "_ "
    
    print(word_display)
    
    if all(letter in guesses for letter in word):
        print("Congratulations! You guessed the word.")
        break
    print(f"You have {turns} turns left.")
    if turns == 0:
        print(f"Game over! The word was: {word}.")
