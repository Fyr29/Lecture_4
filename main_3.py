import random

amount = (random.randint(3, 10))
spisok = []

for i in range(amount):
    spisok.append(random.randint(0, 10))

print(spisok)

spisok_2 = [spisok[0], spisok[2], spisok[-2]]

print(spisok_2)
