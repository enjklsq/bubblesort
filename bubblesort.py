from random import randint

n = 10
a = []

for i in range(n):
    a.append(randint(1, 99))
print('Исходный массив ', a)

i = 0
while i < n - 1:
    j = 0
    while j < n - 1 - i:
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
        j += 1
    i += 1

print('Сортировка ', a)
