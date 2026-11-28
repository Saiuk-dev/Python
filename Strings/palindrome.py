text = "madam"
rev1 = ""

rev = text[::-1]

print(rev)

for i in text:
    rev1 = i+rev1

print(rev1)

#palindrome 

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome ")
