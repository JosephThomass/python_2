my_dict={
    'name':'qwerty',
    'age':34,
    'place':'kknd',
    'work':'student',
    'commpany':'NA'

}

for item in my_dict:
    print(my_dict[item])


# items()-- inbuild function to get key value pair as list
print(my_dict.items())

# values()-- inbuiuld function to get values in dictionary
print(my_dict.values())

# keys()-- inbuild functin to get keys in dictionary.
print(my_dict.keys())


# Iterate to values using value() as range 
for i in my_dict.values():
    print(i)
# Iterate throug keys using key() as range
for i in my_dict.keys():
    print(i)
# Iterative through items as list using items() as function
for i in my_dict.items():
    print(i)