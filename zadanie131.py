import urllib.request, urllib.parse, urllib.error
import json
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_972825.json'
www = urllib.request.urlopen(url, context=ctx).read()

info = json.loads(www)
pel = []

for xxx in info['comments']:
    pel.append(xxx)

x = []
for value in pel:
   x.append(value['count'])

y = []
for l in x:
    v = int(l)
    y.append(v)
import numpy as np
xx = np.sum(y)
print(xx)
