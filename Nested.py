foods = []
Price = []
total = 0

while True:
    food = input("Enter the Food You Want to Buy (Press q to Quit): ")
    if food == "q":
        break
    else:
        price = float(input(f"Enter the price of the {food}"))
        foods.append(food)
        Price.append(price)

print("---- Your Cart ----")
for food in foods:
    print(food, end=" ")

for price in Price:
    total += price

print(total)