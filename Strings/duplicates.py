text = "programming"
result = ""
seen = set()
t1 = ""

for i in text:
    if i not in seen:
        result += i
        seen.add(i)

print(result)

for i in text:
    if i not in t1:
        t1 += i

print(t1)

seen = set()
for i in text:
    if i not in seen:
        result += i
        seen.add(i)
print(seen)