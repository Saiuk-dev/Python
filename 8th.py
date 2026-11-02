import random

low = 1
high = 100

answer = random.randint(low,high)
guess = 0
running = True

print("Welocome To Python Number Guessing Game")
print(f"Enter A Number Between {low} and {high}")


while running:
    g1 = input("Enter Your Guess:")

    if g1.isdigit():
        g1 = int(g1)
        guess += 1

        if g1<low or g1>high:
            print("Entered Number is Out of Range")
            print(f"Enter A Number Between {low} and {high}")
        elif g1<answer:
            print("Too Low! ")
        elif g1>answer:
            print("Too High! ")
        else:
            print(f"Correct !!! The Answer Was {answer}")
            print(f"You took {guess} no. of guess")
            break

    else:
        print("Invalid Guess")
        print(f"Enter A Number Between {low} and {high}")