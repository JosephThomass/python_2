class Student:
    def __init__(self):
        self.name=""
        self.place=""
        self.department=""
    def set_detail(self):
        self.name=input("Enter name : ")
        self.place=input("Enter place: ")
        self.department=input("Enter Department: ")

    def display(self):
    
        print("________Student details________")
        print("Student Name: ",self.name)
        print("Student Place: ",self.place)
        print("________________________________")
obj=Student()
obj.set_detail()
obj.display()

obj1=Student()
obj.set_detail()
obj.display()

