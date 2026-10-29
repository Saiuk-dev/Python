import time

time1 = int(input("Enter time in seconds "))

for x in reversed(range(0,time1)):
    seconds = x%60
    minutes = int(x/60)%60
    hours = int(x/3600)
    print(f"{hours}:{minutes}:{seconds}")
    time.sleep(1)

print("Wake up bud!!")