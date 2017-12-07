import copy

fstream = open("input.txt")

for line in fstream:
	line = ((line.split()))
	line = [int(x) for x in line]
	length = len(line)
	#print(line)

checkerlist = []

newline = copy.deepcopy(line)

count = 0

while True:
	print(newline)
	count += 1
	maxbank = max(newline)
	#print(maxbank)
	maxbankindex = newline.index(maxbank)
	for i in range(0, length):
		#print("loop")
		if(i != maxbankindex):
			newline[i] += (maxbank // (length - 1))
			#print(newline[i])
		else:
			newline[i] = (maxbank % (length - 1))


	newline = [str(x) for x in newline]
	temp = ''.join(newline)
	bc = 0
	for j in range(0, len(checkerlist)):
		if(temp == checkerlist[j]):
			#print(newline, "break")
			bc = 1
			break
	if(bc == 1):
		break

	#print(newline)
	checkerlist.append(temp)
	#print(checkerlist)

	newline = [int(x) for x in newline]


print(newline)
print(count)