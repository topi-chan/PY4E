#Write a program that prompts for a file name, then opens that file and
#reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines
#and compute the average of those values and produce an output as shown below.
#Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
#when you are testing below enter mbox-short.txt as the file name.
c = 0.0
count = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()
#    if line.startswith("X-DSPAM"):
#        count = count + 1
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    #print(line)
    #print(pos)
    pos = line.find(" ")
    x = (line[pos+1:])
    y = float(x)
    if y > 0.0:
        count = count +1
    if y > 0.0:
        c = y + c
z = c / count
print("Average spam confidence:", z)
