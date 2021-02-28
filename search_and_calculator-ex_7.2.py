# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
nums = 0
alines= 0
for line in fh:
  if not line.startswith("X-DSPAM-Confidence:") :
    continue
  count = count + 1
  nums = nums + float(line[20:])
  
  alines = alines + nums
  average = nums/count

print("Average spam confidence:", average)
