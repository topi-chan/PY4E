fname = input("Podaj nazwę pliku: ")
if len(fname) < 1: fname = 'clown.txt'
hand = open(fname)

dic = dict()
for lin in hand:
    lin = lin.rstrip()
    #print(lin)
    wds = lin.split()
    #print(wds)
    for w in wds:
        dic[w] = dic.get(w,0) + 1



largest = -1
word = None
for k,v in dic.items():
#    print(k,v)
    if v > largest:
        largest = v
        word = k
print('Podsumowując: ', word, largest)


#            print("**JUŻ JEST**")
#        else:
#            dic[w] = 1
#            print("**NOWE!**")
#print(dic)
#        print(w, dic[w])
