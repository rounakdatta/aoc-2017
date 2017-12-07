from anytree import Node, RenderTree

def secfun(myarr, i)	:
	for j in range(3, len(myarr[i])):	#each element of the line
				#print(myarr[i][j])
				for k in range(0, len(myarr)):	#each line checking again
					if((len(myarr[k]) != 0) and (len(myarr[i]) != 0)):
						if(myarr[i][j].replace(',','') == myarr[k][0]):
							#print("this is ")
							#print(myarr[k][0])
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

#myarr = [item for sublist in myarr for item in sublist]
for i in range(0, len(myarr)):
	#print(myarr[i])
	if(len(myarr[i]) < 3):
		del myarr[i][:]

myarr = [x for x in myarr if x != []]

myarr = check(myarr)

myarr = [x for x in myarr if x != []]

for i in range(0, len(myarr)):
	print(myarr[i])

print(myarr[0][0])

'''
counter = 0
while(len(myarr) > 1):
	if(len(myarr[counter] > 2)):
		subelements = myarr[counter][3:]
		for i in range(0, len(subelements)):
			'''
