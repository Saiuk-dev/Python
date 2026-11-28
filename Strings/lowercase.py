text = "hello"
result = ""
conversion = { 'h':'H', 'e':'E' , 'l':'L', 'o':'O'}

for i in text:
    if i in conversion:
        result += conversion[i]
    else:
        result += i

print(result)