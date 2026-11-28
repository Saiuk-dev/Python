text = "today is a wonderfull day "

result = text.replace(" ","")

print(result)

r1 = ""

for i in text:
    if i!=" ":
        r1 += i

print(r1)