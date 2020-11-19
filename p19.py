maly = 99
print'Before', maly
for num in 9, 41, 12, 3, 74, 15:
    if num < maly:
        maly = num
    print maly, num
print'After', maly
print''
print''
print''
maly = None
print'Before', maly
for num in 9, 41, 12, 3, 74, 15:
    if maly is None:
        maly = num
    elif num < maly:
        maly = num
        print maly, num
print'After', maly
print''
print''
print''
num = 0
tot = 0.0
while True:
    sval = input('Enter a number: ')
    fval = float(sval)
