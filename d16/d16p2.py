programs = []
#programs = ['a', 'b', 'c', 'd', 'e']
for i in range(97, 113):
	  programs.append(chr(i))


x = []
txt = ''
with open("input.txt") as f:
	while True:
		c = f.read(1)
		if not c:
			x.append(txt)
			break
		if(c == ','):
			x.append(txt)
			txt = ''
		else:
			txt = txt + c
for k in range(0, 1000000000):
	for i in range(len(x)):
		query = x[i]

		if(query[0] == 's'):
			temp = programs[len(programs) - int(query[1:]):]
			programs = programs[:len(programs) - int(query[1:])]
			programs = temp + programs
			#print(''.join(programs))

		elif(query[0] == 'x'):
			params = query.split('/')
			programs[int(params[0][1:])], programs[int(params[1])] = programs[int(params[1])], programs[int(params[0][1:])]
			#print(''.join(programs))

		elif(query[0] == 'p'):
			params = query.split('/')
			el1 = ''.join(params[0][1:])
			el2 = params[1]
			el1 = programs.index(el1)
			el2 = programs.index(el2)
			programs[el1], programs[el2] = programs[el2], programs[el1]
			#print(''.join(programs))

print(''.join(programs))