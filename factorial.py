num=int (input("Enter first number : "))
result =1
if num ==0:
    print(result)
elif num <= 0:
    print("Negative input")

else:
    for i in range(1,num+1):
        result *=i

    print(result)