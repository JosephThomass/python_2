def calculate_hcf(num1,num2):
    if num1<num2:
        small=num1
    else:
        small=num2
    for i in range (1,small+1):
        if(num1%i==0 and num2%i==0):
            hcf=i
    return hcf


num1= int(input("Enter first number : "))
num2= int(input("Enter second number: "))
print(f"HCF if {num1} and {num2} is {calculate_hcf(num1,num2)}")