row=int(input("enter number of row: "))
# for num in range (row+1):
#     print("* " *num)

for i in range (row,0,-1):
    for j in range (i,0,-1):
        print('*' ,end=" ")
    print()