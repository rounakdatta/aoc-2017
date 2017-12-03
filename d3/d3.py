x = input("Value? ")
x = int(x)

i = 2
hor = 0
vert = 0
step = 0
m0 = 0 #applicable on m2
m1 = 0 #applicable on m3
m2 = 0 #applicable on m0
m3 = 0 #applicable on m1
j = 0
while (i <= x):

  if(step == 0):
    #print("step", 0)
    if(j <= (m2 + 1)):
      hor += 1
      j += 1
    m0 = j
    if(j == (m2 + 1)):
      step = (step + 1) % 4
      j = 0
  
  elif(step == 1):
    #print("step", 1)
    if(j <= (m3 + 1)):
      vert += 1
      j += 1
    m1 = j
    if(j == (m3 + 1)):
      step = (step + 1) % 4
      j = 0
  
  elif(step == 2):
    #print("step", 2)
    if(j <= (m0 + 1)):
      hor -= 1
      j += 1
    m2 = j
    if(j == (m0 + 1)):
      step = (step + 1) % 4
      j = 0
  
  elif(step == 3):
    #print("step", 3)
    if(j <= (m1 + 1)):
      vert -= 1
      j += 1
    m3 = j
    if(j == (m1 + 1)):
      step = (step + 1) % 4
      j = 0
    
  print(i, ": horizontal is ", hor, " and vertical is ", vert)
  i += 1
  
print("Total travelling distance is ", (abs(hor) + abs(vert)))
  
  