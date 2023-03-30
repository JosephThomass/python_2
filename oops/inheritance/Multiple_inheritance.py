class Parent1:
    def parent1_info(self):
        print("Parent one info")
class parent2:
    def parnet2_info(self):
        print("parent 2 info from second class")
class child(Parent1,parent2):
    def child_info(self):
        print("child class info inrieted from parent 1  and parent 2")



obj=child()
obj.child_info()
obj.parent1_info()
obj.parnet2_info()
