import random

amount = (random.randint(3, 10))

spisok = [random.randint(0, 10) for i in range(amount)]

spisok_2 = [spisok[0], spisok[2], spisok[-2]]

print(f'{spisok} => {spisok_2}')