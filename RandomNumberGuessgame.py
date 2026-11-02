import random

low = 1
high = 100
guess = 0
answer = random.randint(low,high)
guess = 0
running = True

print("Python Number Guesser Game")
print(f"Select a number between {low} - {high}")

while running:
    g1 = input("Enter Your Guess:")
    
    if g1.isdigit():
        g1 = int(g1)
        guess += 1


        if g1<low or g1>high:
            print("Enter a Smaller digit ")
            print(f"Select a number between {low} - {high}")

        elif g1<answer:
            print("Two low! Try Again!")

        elif g1>answer:
            print("Too High! Try Again!")

        else:
            print(f"Correct the Answer was {answer}")
            print(f"You Took {guess} no. of guess")
            break

    else:
        print(f"Select a number between {low} - {high}")