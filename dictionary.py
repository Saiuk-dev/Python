capitals = {"India": "Delhi", "USA":"America", "China":"Beijing", "Russia":"Moscow","Japan":"Tokyo"}

#print(help(capitals))
#print(capitals.get("India"))

#if capitals.get("Japan"):
 #   print("Capttal exists")
#else:
  #  print("It does not exist")

#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())
capitals.update({"Afghanistan":"Pakistan"})
print(capitals.items())
capitals.update({"Afghanistan":"Kabul"})
print(capitals.items())

for key,value in capitals.items():
    print(key,":",value)

