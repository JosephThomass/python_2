def sum(num1,num2):
    print(num1+num2)
def difference(num1,num2):
    print(num1-num2)
def multiplication(num1,num2):
    print(num1*num2)
def division(num1,num2):
    print(num1/num2)
print('''Select a option
1.sum
2.Substraction
3.Multiplication
4.Division''')
select1=int(input(">"))
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
if select1==1:
    sum(num1,num2)
elif select1==2:
    difference(num1,num2)
elif select1==3:
    multiplication(num1,num2)
elif select1==4:
    division(num1,num2)
else: 
    print("Invalid operation selected")