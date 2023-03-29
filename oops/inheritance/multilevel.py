#********************************* Multilevel inheritance*******************************!!!
class Class1:
    def function1(self):
        print("Fist function")

class Class2(Class1):
    def function2(self):
        print("Second Functiona from second class")
class Class3(Class2):
    def function3(self):
        print("Function 3 from thid clsas")



obj=Class3()
obj.function1()
obj.function2()
obj.function3()