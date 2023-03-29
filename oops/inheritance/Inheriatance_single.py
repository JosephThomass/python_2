class College:
    def __init__(self,cname,place):
        self.cname=cname
        self.place=place
    def display_details(self):
        print("College name is ",self.cname)
        print("Collage Location is : ",self.place)

class Department(College):
    def __init__(self, id, dname):
        self.id=id
        self.dname=dname
        
    def Depart(self):
        print("Inside Child Class")
        print("Depatment ",self.id)
        print("department name "),self.dname


obj1=College("SJCET","KTYM")
# obj1.Depart()
obj1.display_details()
obj2=Department("CSE23","CSE")
obj2.Depart()