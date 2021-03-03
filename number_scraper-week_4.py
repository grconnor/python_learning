from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1159800.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,"html.parser")

sum=0

tags = soup('span')

for tag in tags:
  singlespan=str(tag)
  num = re.findall("[0-9]+",singlespan)
  for nums in num:
    nums=int(nums)
    sum=sum+nums
print(sum)