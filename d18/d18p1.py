def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

f = open("input.txt")

acode = []

mylist = ['a', 0, 'b', 0, 'f', 0, 'i', 0, 'p', 0]

currplay = 0

for line in f:
	line = line.split(' ')
	if(len(line) == 3):
		line[2] = line[2][:-1]
	elif(len(line) == 2):
		line[1] = line[1][:-1]


	
	acode.append(line)

#print(acode)

i = 0

while(i < len(acode)):
	print(acode[i])

	if(acode[i][0] == 'set'):
		if(is_number(acode[i][2])):
			mylist[mylist.index(acode[i][1]) + 1] = acode[i][2]
		else:
			mylist[mylist.index(acode[i][1]) + 1] = mylist[mylist.index(acode[i][2]) + 1]
		i += 1

	elif(acode[i][0] == 'add'):
		if(is_number(acode[i][2])):
			mylist[mylist.index(acode[i][1]) + 1] = str(int(mylist[mylist.index(acode[i][1]) + 1]) + int(acode[i][2]))
		else:
			mylist[mylist.index(acode[i][1]) + 1] = str(int(mylist[mylist.index(acode[i][1]) + 1]) + int(mylist[mylist.index(acode[i][2]) + 1]))
		i += 1

	elif(acode[i][0] == 'mul'):
		if(is_number(acode[i][2])):
			mylist[mylist.index(acode[i][1]) + 1] = str(int(mylist[mylist.index(acode[i][1]) + 1]) * int(acode[i][2]))
		else:
			mylist[mylist.index(acode[i][1]) + 1] = str(int(mylist[mylist.index(acode[i][1]) + 1]) * int(mylist[mylist.index(acode[i][2]) + 1]))
		i += 1

	elif(acode[i][0] == 'mod'):
		if(is_number(acode[i][2])):
			mylist[mylist.index(acode[i][1]) + 1] = str(int(mylist[mylist.index(acode[i][1]) + 1]) % int(acode[i][2]))
		else:
			mylist[mylist.index(acode[i][1]) + 1] = str(int(mylist[mylist.index(acode[i][1]) + 1]) % int(mylist[mylist.index(acode[i][2]) + 1]))
		i += 1

	elif(acode[i][0] == 'snd'):
		currplay = mylist[mylist.index(acode[i][1]) + 1]
		i += 1

	elif(acode[i][0] == 'rcv'):
		if(acode[i][1] != '0'):
			print(currplay)
			break
		i += 1

	elif(acode[i][0] == 'jgz'):
		if(mylist[mylist.index(acode[i][1]) + 1] != '0'):
			i += int(acode[i][2])
		else:
			i += 1

