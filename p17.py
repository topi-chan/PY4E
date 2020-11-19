lala = -1
print'before', lala
for num in [1, 4, 67, 7, 99, 0]:
    if num > lala:
        lala = num
    print(lala, num)
print'After', lala
