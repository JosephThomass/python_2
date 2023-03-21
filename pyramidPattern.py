row = int(input("Enter row: "))
for count in range (row):
    for space_count in range (row-1,count,-1):
        print ("  ",end="")
    for star_count in range (0,count+1):
        print(" *", end="  ")
    print()

#----------------------------------------------------------------------------------

# row = int(input("Enter row: "))
m=2*row
for i in range (row):
    for j in range (m):
        print(end=" ")
    m=m-1
    for j in range (i+1):
        print("*", end=" ")
    print()
