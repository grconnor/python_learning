import re

ui = input('Enter a file name: ')
if len(ui) < 8:
  ui = "actual_data.txt"

handle = open(ui)

lst = list()
count = 0

for line in handle:
  lst = re.findall('[0-9]+', line)

  for x in lst:
    count = count + int(x)
    
print(count)