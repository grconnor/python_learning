total = 0
count = 0

while True:
  uinput = input("Enter in numbers, type 'done' to get the results: ")

  if uinput == "done":
    break
  value = float(uinput)
  total = total + value
  count = count + 1

average = total / count
print("Average: ", average)