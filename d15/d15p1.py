gen1 = 783
gen2 = 325

count = 0

for i in range(0, 40000000):
	gen1 = (gen1 * 16807) % 2147483647
	gen2 = (gen2 * 48271) % 2147483647
	if((bin(gen1)[-16:]) == (bin(gen2)[-16:])):
		count += 1

print(count)