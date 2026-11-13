rev = "Coldwars"

s3 = rev[::-1]

print(s3)

# Check palindrome

s = input("enter a string: ")
s1 = input('ENter a string: ')

if s == s[::-1]:
    print("Palindrome")
else:
    print("not a palindrome ")

rev = ""
for char in s1:
    rev = char + rev

if s1 == s1[::-1]:
    print("Palindrome")
else:
    print("not a palindrome ")

# Prime number 

n = int(input("Enter a number: "))

for i in range(2,n):
    if n%i == 0:
        print("Not prime")
        break
    else:
        print("prime")

    # factorial

k = int(input("Enter a number to find the factorial "))

fact = 1

for j in range(1,n+1):
    fact = fact*j

print("Factorial: ",fact)