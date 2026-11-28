text = "Hello my name is sai"
words = text.split()
result = []

for i in words:
    result.append(i[::-1])

print(" ".join(result))


#to reverse a whole string 
r2 = text[::-1]
print(r2)
rev = ""
for i in text:
    rev = i + rev

print(rev)