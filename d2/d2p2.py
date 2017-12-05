import fileinput

s = 0

for line in fileinput.input():
	b = 0
	line = ((line.split()))
	line = [int(i) for i in line]
	for i in range(0, len(line)):
		for j in range(0, len(line)):
			if(((line[i] % line [j]) == 0) and i != j):
				b = 1
				print(line[i], " and ", line[j])
				s += (line[i] // line[j])
				break
			if(b ==1):
				break

print(s)
	
