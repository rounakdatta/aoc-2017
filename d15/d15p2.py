gen1 = 783
gen2 = 325

count = 0
list1 = []
list2 = []

count1 = 0
while(count1 < 5000000): #5000000
	gen1 = (gen1 * 16807) % 2147483647
	if(gen1 % 4 == 0):
		#print(gen1)
		list1.append(gen1)
		count1 += 1
		#if((bin(gen1)[-16:]) == (bin(gen2)[-16:])):
			#count += 1

count2 = 0
while(count2 < 5000000): #5000000
	gen2 = (gen2 * 48271) % 2147483647
	if(gen2 % 8 == 0):
		#print(gen2)
		list2.append(gen2)
		count2 += 1
		#if((bin(gen1)[-16:]) == (bin(gen2)[-16:])):
			#count += 1

#print(len(list1))
#print('hello')
#print(len(list2))

i = 0
j = 0
while((i < len(list1)) and (j < len(list2))):
	if((bin(list1[i])[-16:]) == (bin(list2[j])[-16:])):
		#print(list1[i])
		#print(list2[i])
		count += 1
	i += 1
	j += 1

print(count) #309