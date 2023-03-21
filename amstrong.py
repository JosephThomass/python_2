num = int(input("Enter the number: "))
temp =num
count=num
ans=0
while (count>0):
    ans=ans+1
    count=count //10
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**ans
    temp=temp//10
if num==sum:
    print(f"{num} is a Amstrong number")
else:
    print(f"{num} is not a Amstrong number")



