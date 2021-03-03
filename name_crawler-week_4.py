import urllib.request
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
count = input('Enter count: ')
icount = int(count)
pos = input('Enter position: ')
ipos = int(pos)
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags_lst = list()

for x in range(0,icount):
  tags = soup('a')
  atags = tags[ipos-1]
  needed_tag = atags.get('href', None)
  url = str(needed_tag)
  html = urllib.request.urlopen(url).read()
  soup = BeautifulSoup(html, 'html.parser')
  print(atags.get('href', None))