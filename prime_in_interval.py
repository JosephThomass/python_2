min_interval=int(input("Enter the lover limit: "))
max_interval=int(input("Enter the maximum limit:  "))

for num in range(min_interval,max_interval):
    for i in range(2,num//2):
        if num%i==0:
            break
    else:
        print(f"{num}")
