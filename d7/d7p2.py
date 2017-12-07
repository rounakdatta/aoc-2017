from anytree import Node, RenderTree

def searchandcalc(currval):
	temp = []
	suma = []
	for sublist in myarr:
		if(sublist[0] == currval):
			temp = sublist
			break
	#print(temp)
	if(len(temp) < 3):
		thisone = Node(temp[0], parent=treearr[-1])
		treearr.append(thisone)
		#justacounter += 1
		return int(temp[1][1:][:-1])
	else:
		tv = 0
		for i in range(3, len(temp)):
			tv = searchandcalc(temp[i].replace(',',''))
			suma.append(tv)
			if((None not in suma) and (len(suma) == 3) and ((suma[1:] == suma[:-1]) == False)):
				print(temp[0])
				print(suma)
			return int(sum(suma))


fstream = open("input.txt", "r")

myarr = []

for line in fstream:
	line = line.split()
	myarr.append(line)

rootval = 'eqgvf'
currval = rootval

treearr = []
neww = Node(rootval)
treearr.append(neww)
#justacounter = 0

searchandcalc(rootval)

print(neww.children)