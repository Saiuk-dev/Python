menu = {"Pizza":150,
         "Burger":150,
         "Cold Coffee":150,
         "Honey-Chilli potato":170,
         "French Fries":170,
         "Diet-Coke":90,
         "Shwarma":120,
         "Water Bottle":20}

cart = []
total = 0

for key,value in menu.items():
    print(f"{key:20}:  {value}")

while True:
    food = input ("Select an item (q to quit): ")
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is {total}")