#   *args
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1,2,3,4,5,6,7,8,9))

def print_address ( ** kwargs) :
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake St.",
city="Detroit",
state="MI",
zip="54321")