import fileinput

s = 0
for line in fileinput.input():
	#print(int(max(line.split(), key=len)) - int(min(line.split(), key=len)))
	line = ((line.split()))
	line = [int(i) for i in line]
	#print(max(line) - min(line))
	s += (max(line) - min(line))

print(s)
	
