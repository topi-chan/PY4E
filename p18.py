liczba = 0
print'Przed', liczba
for numer in 9, 41, 12, 3, 74, 15:
    liczba = liczba + numer
    print liczba, numer
print'Po', liczba
print''
print''
count = 0
sum = 0
print'Before', count, sum
for value in 9, 41, 12, 3, 74, 15:
    count = count + 1
    sum = sum + value
    print count, sum, value
print'After', count, sum, sum / count
print''
print''
print'Before'
for wartosci in 9, 41, 12, 3, 74, 15:
    if wartosci > 20:
        print'Large number', wartosci
print'After'
print''
print''
boolean = False
print'Before', boolean
for wartosc in 9, 41, 12, 3, 74, 15:
    if wartosc == 3:
        boolean = True
    print boolean, wartosc
print'After', boolean
print''
print''
