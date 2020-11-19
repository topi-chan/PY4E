lib = []
lib0 = []
lib1 = []
lib2 = []
lib3 = []
lib4 = []
lib5 = []
lib6 = []
lib7 = []

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url0 = 'http://py4e-data.dr-chuck.net/known_by_Morwena.html'
html0 = urllib.request.urlopen(url0, context=ctx).read()
soup = BeautifulSoup(html0, 'html.parser')
tags0 = soup('a')
for tag in tags0:
    lib0.append(tag.get('href', None))

url1 = (lib0[17])
html1 = urllib.request.urlopen(url1, context=ctx).read()
soup = BeautifulSoup(html1, 'html.parser')
tags1 = soup('a')
for tag in tags1:
    lib1.append(tag.get('href', None))

url2 = (lib1[17])
html2 = urllib.request.urlopen(url2, context=ctx).read()
soup = BeautifulSoup(html2, 'html.parser')
tags2 = soup('a')
for tag in tags2:
    lib2.append(tag.get('href', None))

url3 = (lib2[17])
html3 = urllib.request.urlopen(url3, context=ctx).read()
soup = BeautifulSoup(html3, 'html.parser')
tags3 = soup('a')
for tag in tags3:
    lib3.append(tag.get('href', None))

url4 = (lib3[17])
html4 = urllib.request.urlopen(url4, context=ctx).read()
soup = BeautifulSoup(html4, 'html.parser')
tags4 = soup('a')
for tag in tags4:
    lib4.append(tag.get('href', None))

url5 = (lib4[17])
html5 = urllib.request.urlopen(url5, context=ctx).read()
soup = BeautifulSoup(html5, 'html.parser')
tags5 = soup('a')
for tag in tags5:
    lib5.append(tag.get('href', None))

url6 = (lib5[17])
html6 = urllib.request.urlopen(url6, context=ctx).read()
soup = BeautifulSoup(html6, 'html.parser')
tags6 = soup('a')

for link in soup.find_all('a'):
    lib.append(link.contents[0])
print(lib[17])
