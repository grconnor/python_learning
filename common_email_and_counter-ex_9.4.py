name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

senders = dict()
bigcount = None
cmail = None

for line in handle:
  if line.startswith("From "):
    splitted = line.split()
    address = splitted[1]
    senders[address] = senders.get(address, 0) + 1
        
for email, count in senders.items():
  if bigcount is None or count > bigcount:
    cmail = email
    bigcount = count

print(cmail, bigcount)