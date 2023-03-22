my_dict={
    'name':'qwerty',
    'age':34,
    'place':'kknd',
    'work':'student',
    'company':'NA'

}

print(my_dict)

# adding new key value pair to the dictionary

my_dict['martial status']='single'


# Updated the dictionary
my_dict['work']='Engineer'
my_dict['company']='x-team'


print(my_dict)

# delete value from list using pop() and del method

del my_dict["age"]
my_dict.pop('work')


print(my_dict)