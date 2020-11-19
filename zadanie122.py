#Data Format
#The file is a table of names and comment counts. You can ignore most of the data
#in the file except for lines like the following:
#<tr><td>Modu</td><td><span class="comments">90</span></td></tr>
#You are to find all the <span> tags in the file and pull out the numbers from the
#tag and sum the numbers.
#Look at the sample code provided. It shows how to find all of a certain kind of tag,
# loop through the tags and extract the various aspects of the tags.
# Retrieve all of the anchor tags

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
import re
lib = []
tags = soup('span')
for tag in tags:
    lib.append(tag.contents[0])
#print(lib)
x = []
for l in lib:
    l = str(l.encode('utf-8'))
#print(res)
for l in lib:
    v = int(l)
    x.append(v)
#print(x)
ls = [type(z) for z in x]
#print(ls)
import numpy as np
xx = np.sum(x)
print(xx)
