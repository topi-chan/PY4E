#Write a program to read through the mbox-short.txt and figure out the
#distribution by hour of the day for each of the messages. You can pull the
#hour out from the 'From ' line by finding the time and then splitting the
#string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts,
#sorted by hour as shown below.
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
counts = dict()
for line in fh:
    line = line.rstrip()
    if not line.startswith("From"):
        continue
    if line.endswith("2008"):
         x = line.split()
         y = x[-2]
         z = list()
         z.append(y[0:2])
         for word in z:
             counts[word] = counts.get(word,0) + 1
sd = sorted(counts.items())
for k,v in sd:
    print(k, v)





#            print(lis)


#t = sorted(d.items())


#    pos = line.find("2008")
#    x = (line[pos-9:])
#    xline = line
