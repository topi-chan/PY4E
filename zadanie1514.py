import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

import re

lista = []
listapro = []

fh = open('mbox.txt')
for line in fh:
     if not line.startswith('From: '):
         continue
     pieces = line.split()
     x = re.findall('.+?@(.+?)\s', line)
     lista.append(x)
for l in lista:
    for item in l:
        item = str(item)
        listapro.append(item)
for y in listapro:
     cur.execute('SELECT count FROM Counts WHERE org = ? ', (y,))
     row = cur.fetchone()
     if row is None:
         cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (y,))
     else:
         cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (y,))
conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
