questions = (
    "Who was the first man to step on the Moon?",
    "Which chemical element has the symbol 'Au'?",
    "What is the smallest unit of life that can replicate independently?",
    "Who wrote the play 'Romeo and Juliet'?",
    "What is the largest mammal in the world?",
    "Which country is known as the Land of the Rising Sun?"
)

options = (
    ("A: Yuri Gagarin", "B: Neil Armstrong", "C: Buzz Aldrin", "D: Michael Collins"),
    ("A: Silver", "B: Gold", "C: Iron", "D: Copper"),
    ("A: Tissue", "B: Cell", "C: Organ", "D: Organism"),
    ("A: William Shakespeare", "B: Charles Dickens", "C: Leo Tolstoy", "D: Mark Twain"),
    ("A: African Elephant", "B: Blue Whale", "C: Giraffe", "D: Hippopotamus"),
    ("A: China", "B: Japan", "C: Thailand", "D: South Africa")
)

answers = ("B", "B", "B", "A", "B", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("---------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    
    if guess == answers[question_num]:
        print("CORRECT")
        score += 1
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    
    question_num += 1

print(f"\nYour final score is {score} out of {len(questions)}")
