#Find the link at position 3 (the first name is 1). Follow that link. Repeat this
#process 4 times. The answer is the last name that you retrieve.
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

lib = []
x = []
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
#    lib.append(tag.contents[0])
#for l in lib:
#    l = str(l.encode('utf-8'))
#    v = str(l)
#    x.append(v)
#ls = [type(v) for v in x]
#print(lib)
#print(x)
