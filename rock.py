import random

options = ("Rock","Paper","Scissors")
player = None
c1 = 0
p1 = 0
t1 = 0
k = 5
#computer = random.choice(options)

for round in range(1,6):
    player = None
    while player not in options:
        
        player = input("Enter Your Choice: ").strip().capitalize()
    computer = random.choice(options)
    print(f"Computer: {computer}")
    
    if player == computer:
     t1 += 1
     print("Its a Tie !!!")
    elif player == "Rock" and computer == "Paper":
        c1 += 1
        print("Computer Win !!!")
    elif player == "Paper" and computer == "Scissors":
        c1 += 1
        print("Computer  Win !!!")
    elif player == "Scissors" and computer == "Rock":
        c1 += 1
        print("Computer Win !!!")
    elif player == "Paper" and computer == "Rock":
        p1 += 1
        print("Player Win !!!")
    elif player == "Rock" and computer == "Scissors":
        p1 += 1
        print("Player Win !!!")
    elif player == "Scissors" and computer == "Paper":
        p1 += 1
        print("Player Win !!!")

print(f"You won {p1} times")
print(f"Computer won {c1} times")
print(f"It was a tie {t1} times")