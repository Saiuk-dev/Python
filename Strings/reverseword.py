text = "Hello my name is sai"
words = text.split()
result = []

for i in words:
    result.append(i[::-1])

print(" ".join(result))

