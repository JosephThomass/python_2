[]

set1={'a','b','c','d'}
set2={'d','e','f','g'}
set3={'f','g','h','i'}
# union

# using union function
print("Union operation using function: ")
print(set1.union(set2))
# using | opertator
print("Union operation using operator: ")
print(set1 | set2 | set3)

# intersection

# using function
print("intersection operation usin function: ")
print(set1.intersection(set2))
# using & operator
print("intersection operation using opertator: ")
print(set1&set2)

# DIFFERENCE
# using 
print("Difference operation using function: ")
print(set1.difference(set2))

# using - opertator
print(set1-set2-set3)

# SYMATRIC DIFFERENCE
# using function
print("Symmentric difference operation using function: ")
print(set1.symmetric_difference(set2))
# using ^ operator
print("Symmentric difference operation using operartor: ")
print(set1 ^ set2)

