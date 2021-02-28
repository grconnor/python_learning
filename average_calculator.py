total = 0
count = 0

while True:
  input = input("Enter in numbers, type 'done' to get the results")

  if input == "done":
    break
  value = float(input)
  total = total + value
  count = count + 1

average = total / count
print("Average: ", average)