import json
import urllib.request, urllib.parse, urllib.error

url = input("Enter a url: ")
data = urllib.request.urlopen(url).read()
data = json.loads(data)
total = 0

for user in data['comments']:
  total = total + user['count']

print('Total comments:', total)