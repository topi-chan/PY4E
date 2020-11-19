counts = dict()
print("Wprowadź tekst: ")
line = input('')
words = line.split()
print("Słowa: ", words)
print("Liczę...")
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Liczba słów: ', counts)
for znak in counts:
    print(znak, counts[znak])
