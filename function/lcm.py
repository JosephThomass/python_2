def calcu_lcm(num1,num2):
    if(num1>num2):
        great=num1
    else:
        great=num2
    while(True):
        if((great%num2==0 and (great%num1==0))):
            lcm=great
            break
        else:
            great +=1
    return lcm


num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
print(f"LCM of {num1} and {num2} is {calcu_lcm(num1,num2)}")