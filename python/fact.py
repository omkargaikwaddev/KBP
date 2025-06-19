rows = 4

for i in range(rows,0,-1):
    for j in range(rows-i):
     print(" ",end="")

    for j in range(i):
       if (i+j) % 2 == 0:
          print("1",end=" ")
       else:
          print("0",end=" ")
    print()