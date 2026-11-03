list_price = float(input("Enter Your MRP: "))


def bill(list_price,Discount=0,Tax=0.10):
    Discount = Discount / 100
    Tax = Tax / 100
    return list_price * (1-Discount) * (1+Tax)

print(f"Final Bill: ₹{bill(list_price):.2f}")