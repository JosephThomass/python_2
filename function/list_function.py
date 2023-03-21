def reverse_list(mylist):
    return mylist[::-1]
mylist=[]
limit=int(input("Enter the size of the list: "))


for i in range(limit):
    item=input(">")
    mylist.append(item)

revlist= reverse_list(mylist)
print(revlist)
