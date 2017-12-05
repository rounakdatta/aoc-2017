contents=input()
i = 0
sum = 0
while(i < len(contents)):
  if (contents[i] == contents[(i + (len(contents) // 2)) % len(contents)]):
    sum += int(contents[i])
  i += 1
print(sum)
