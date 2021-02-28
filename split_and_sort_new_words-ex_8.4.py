fname = input("Enter file name: ")
fh = open(fname)

lst = list()

for lines in fh:
  splitted = lines.split()

  for word in splitted:
    if word not in lst:
      lst.append(word)
            
lst.sort()
print(lst)
