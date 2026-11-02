import random

num = random.randint(1,7)
print(num)


options = ("Rock","Paper","Scisorss")
option = random.choice(options)
print(option)

cards = ["2","3","A","4","N","6","1","F","7"]
random.shuffle(cards)
print(cards)