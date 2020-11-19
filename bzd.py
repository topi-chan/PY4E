dict = dict()
dict = {'Diazepam': 1, 'Lorazepam': 0.1, 'Klonazepam': 0.05, 'Oksazepam': 2}
lek = input("Podaj nazwę substancji lub leku: ")
if lek in dict:
    dawka = input("Ile substancji zażyłeś w mg? (dawki po przecinku podaj z kropką, np. 0.5, bez mg na końcu)")
    if dawka == '0':
        print("W takim razie jesteś trzeźwy, gratuluję :)")
        quit()
else:
    print("Nie rozpoznano substancji")
    quit()
ekwiwalent = input("Podaj nazwę substancji lub leku, na które chcesz przeliczyć: ")
d = float(dawka)
if ekwiwalent in dict and lek in dict:
    x = dict[ekwiwalent] * (dict[lek] * d)
    print(x, " mg")
else:
    print("błąd")
    quit()
