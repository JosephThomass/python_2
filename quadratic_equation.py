from math import *
a=float(input("enter the value of A: "))
b=float(input("enter the value of B: "))
c=float(input("enter the value of C: "))
print("------------------------------")

r= b**2-4*a*c

if r>0:
    x1=((-b)+sqrt(r))/2*a
    x2=((-b)-sqrt(r))/2*a
    print(f'The result are {x1} and {x2}')
elif r==0:
    x1=(-b)/2*a
    print(f'The result are {x1}')
else:
    print("Discriminet less than zero")
