import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

handle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in handle:
  print(line.decode().strip())