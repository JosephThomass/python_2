def addSum(num1, num2):
    return num1+num2, num1 - num2
a= int(input(">"))
b= int(input(">"))
result1, result2=addSum(a,b)
print(f'sum={result1} \nDiffernece={result2}')