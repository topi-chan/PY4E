import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_972824.xml'
xml = urllib.request.urlopen(url, context=ctx).read()

tree = ET.fromstring(xml)

lista = []
y = []
elems = tree.findall('.//count')
for x in elems:
    lista.append(x.text)
for l in lista:
    v = int(l)
    y.append(v)
import numpy as np
xx = np.sum(y)
print(xx)
