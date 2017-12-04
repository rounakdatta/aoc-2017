import fileinput

same = 0
count = 0

for line in fileinput.input():
	line = ((line.split()))

	for i in range(0, len(line)):
		line[i] = (list(line[i]))
		line[i].sort()
		line[i] = ''.join(line[i])

	for i in range(0, len(line)):
		for j in range((i + 1), len(line)):
			if(line[i] == line[j]):
				same = 1
				break
		if(same == 1):
			break
	if(same == 0):
		count += 1
	same = 0

print(count)
