import random

amount = (random.randint(5, 15))
spisok = []

for i in range(amount):
    spisok.append(random.randint(0, 2))
print(spisok)

for i in range(spisok.count(0)):
    spisok.remove(0)
    spisok.append(0)

print(spisok)