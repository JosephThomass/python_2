class Employee:
    def __init__(self,id,name,phonenumber,company,emailid,salary):
        self.eid=id
        self.ename=name
        self.emob=phonenumber
        self.ecompany=company
        self.email=emailid
        self.esalary=salary
    def displaydata(self):
        print(f"Name:{self.ename}\nPhone number:{self.emob}\nEmail address:{self.email}\nCompany:{self.ecompany}\nsalary:{self.esalary}")
emp1= Employee(7616,"Emil",9875696842,"Wipro","emil@wipo.inc",56232)

emp1.displaydata()