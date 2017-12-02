import fileinput

s = 0

for line in fileinput.input():
	line = ((line.split()))
	line = [int(i) for i in line]
	s += (max(line) - min(line))

print(s)
	
