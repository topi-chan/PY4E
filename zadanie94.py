#Write a program to read through the mbox-short.txt and figure out who has sent the
#greatest number of mail messages. The program looks for 'From ' lines and takes the
#second word of those lines as the person who sent the mail. The program creates a Python
#dictionary that maps the sender's mail address to a count of the number of times they
#appear in the file. After the dictionary is produced, the program reads through the
#dictionary using a maximum loop to find the most prolific committer.
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
dic = dict()
ls = list()
for w in fh:
    if w.startswith("From "):
        ls.append(w)
    else:
        continue
for l in ls:
    x = l.split()
    y = (x[1])
#    print(y)
    dic[y] = dic.get(y,0) + 1
#    print(dic)
    counts = dict()
    for line in fh:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word,0) + 1
    bigcount = None
    bigword = None
    for word, count in dic.items():
        if bigcount is None or count > bigcount:
            bigword = word
            bigcount = count
print(bigword, bigcount)

#count = len(ls)
#names = ['']
#for name in names :
#    dic[name] = dic.get(name, 0) + 1
#print(dic)
#print(count)
#print("There were", count, "lines in the file with From as the first word")
