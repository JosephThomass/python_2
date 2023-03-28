class MyClass:
    def myfunction(self,name,age):
        print(f"name: {name}\nage:{age}")
obj=MyClass()
mylist=["amal","shyam","sona","Anu","alan"]
for i in mylist:
    name=mylist[i]
    age=23+i
    obj.myfunction(name,age)

    obj.myfunction(name,age)
