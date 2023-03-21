# Function to swap first and last element
def swawpList(mylist):
    size_array=len(mylist)

    temp = mylist[0]
    mylist[0] = mylist[size_array-1]
    mylist[size_array-1] = temp
    return mylist
#Defined a list
mylist=[12,78,56,2,6,3,55,69]
#Called the swaplist function
swawpList(mylist)
print(mylist)
