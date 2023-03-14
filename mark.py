physics=float(input(" Enter Physics mark :"))
maths=float(input(" Enter maths mark :"))
biology=float(input(" Enter biology mark :"))
chem=float(input(" Enter chemistry mark :"))
comp=float(input(" Enter computer mark :"))
print("------------------------------------------\n")
total=physics+maths+comp+chem
print("Total mark: ",total)
percentage= ((total/500)*100)%100
print("Percentage is: ",percentage)

if percentage>=90:
    print("A grade")
elif(percentage >= 80):
    print("B grade")
elif(percentage >= 70):
    print("B grade")
elif(percentage >= 60):
    print("B grade")
else:
    print("Fail")