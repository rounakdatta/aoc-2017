fstream = open("input.txt", "r")

count = 0
myarr = []

for line in fstream:
	n = int(line)
	myarr.append(n)

curr = 0

while(curr != len(myarr)):
	temp = myarr[curr]
	if(myarr[curr] >= 3):
		myarr[curr] -= 1
	else:
		myarr[curr] += 1

	curr += temp
	count += 1

print(count)
print(myarr)