questions = ("How Many Elements are there in periodic table: ",
             "Which Animal Lays the largest eggs: ",
             "What is the most abundent gas on earth: ",
             "How many bones are there in human body: ")

options = (("A. 116","B. 117","C. 118","D. 119"),
           ("A. Whale","B. Crocodile","C. Snake","D. Ostrich"),
           ("A. Nitrogen","B. Oxygen","C. Carbon-Dioxide","D. Hydrogen"),
           ("A. 206","B. 207","C. 208","D. 209"))

answers = ("C","D","A","A")
gueses = []
score = 0
question_num = 0 

for question in questions:
    print("----------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A,B,C,D): ").upper()
    gueses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer: ")

        
    question_num += 1
print(f"Your Score is {score}")