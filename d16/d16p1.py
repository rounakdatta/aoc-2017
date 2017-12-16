programs = ['a', 'b', 'c', 'd', 'e']
#for i in range(97, 113):
#  programs.append(chr(i))

x = input()
x= x.split(',')

for query in x:
  if(query[0] == 's'):
    temp = programs[len(programs) - int(query[1:]):]
    programs = programs[:len(programs) - int(query[1:])]
    programs = temp + programs
    print(''.join(programs))
  if(query[0] == 'x'):
    params = query.split('/')
    programs[int(params[0][1:])], programs[int(params[1])] = programs[int(params[1])], programs[int(params[0][1:])]
    print(''.join(programs))
    #print(params)
  if(query[0] == 'p'):
    params = query.split('/')
    programs[programs.index(params[0][1:])], programs[programs.index(params[1])] = programs[programs.index(params[1])], programs[programs.index(params[0][1:])]
    print(''.join(programs))

#print(''.join(programs))