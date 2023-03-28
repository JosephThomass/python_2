class Myclass:
    def __init__(self,name,age):
        self.Mname=name
        self.mage=age
    def displaydata(self):
        print(f"Name is {self.Mname} age is {self.mage}")

employe=Myclass("jipson",33)
employe2=Myclass("vazha",23)
employe3=Myclass("dinken",32)

employe.displaydata()
employe2.displaydata()
employe3.displaydata()