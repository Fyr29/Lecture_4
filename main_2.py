import random

amount = (random.randint(0, 10))
spisok = []

for i in range(amount):
    spisok.append(random.randint(0, 10))

print(spisok)
print()

summa = sum(spisok[0::2]) * (spisok[-1] if spisok else [])

print(f'{spisok[0::2]} => {summa}')

# print(f'{spisok[0::2]} => (', end='')
# print(*spisok[0::2], sep=' + ', end='')
# print(f') * {spisok[-1] if spisok else 0} = {summa}')