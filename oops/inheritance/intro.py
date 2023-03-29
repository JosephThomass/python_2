class parent1:
    def function1(self):
        print("Inside parent class")
class Child1(parent1):
    def function2(self):
        print("Inside child class")


obj1=Child1()
obj1.function2()
obj1.function1()