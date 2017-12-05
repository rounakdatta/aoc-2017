fstream = open("input.txt", "r")

count = 0
myarr = []

for line in fstream:
	n = int(line)
	myarr.append(n)

curr = 0

while(curr != len(myarr)):
	temp = myarr[curr]
	myarr[curr] += 1

	curr += temp
	count += 1

print(count)
print(myarr)