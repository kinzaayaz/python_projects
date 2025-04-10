questions = [
    "What is the capital of France?",
    "Which planet is known as the Red Planet?",
    "What is the largest ocean on Earth?",
    "Who wrote 'Hamlet'?",
    "What is the square root of 64?"
]
options = [
    "A) Berlin  B) Madrid  C) Paris  D) Rome",
    "A) Earth  B) Mars  C) Venus  D) Jupiter",
    "A) Atlantic  B) Indian  C) Arctic  D) Pacific",
    "A) Shakespeare  B) Dickens  C) Tolstoy  D) Hemingway",
    "A) 6  B) 7  C) 8  D) 9"
]
answers = ["C", "B", "D", "A", "C"]
score = 0
i = 0
while i < len(questions):
    print(questions[i])    
    print(options[i])           
    
    user = input("Your answer : ").upper() 
    if user == answers[i]:      
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is: " + answers[i])
    i=i+1  
print("Your score is:", score, "out of", len(questions))
