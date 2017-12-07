def secfun(myarr, i)	:
	for j in range(3, len(myarr[i])):	#each element of the line
				for k in range(0, len(myarr)):	#each line checking again
					if((len(myarr[k]) != 0) and (len(myarr[i]) != 0)):
						if(myarr[i][j].replace(',','') == myarr[k][0]):
							secfun(myarr, k)
							del myarr[k][:]

def check(myarr):
	for i in range(0, len(myarr)):	#each line
		if(len(myarr[i]) != 0):
			secfun(myarr, i)


	return myarr

fstream = open("input.txt", "r")

myarr = []

for line in fstream:
	line = line.split()
	myarr.append(line)

for i in range(0, len(myarr)):
	if(len(myarr[i]) < 3):
		del myarr[i][:]

myarr = [x for x in myarr if x != []]

myarr = check(myarr)

myarr = [x for x in myarr if x != []]

for i in range(0, len(myarr)):
	print(myarr[i])

print(myarr[0][0])