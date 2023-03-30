class Person:
    def person_info(self,name,age):
        print("++++++++++++++++++++++++++++++++")
        print("Employee Name : ",name)
        print("Employee age: ", age)
class Company():
    def company_info(self,cname,location):
        print("_-------------------------------------_")
        print("Company name :", cname)
        print("Company Location: ",location)
class Employee(Person,Company):
    def empployee_info(self,salary, position):
        print("/////////////////////////////////////")
        print("Employee salay :",salary)
        print("Employee position: ",position)

obj=Employee()

obj.company_info("WAC","Koatty")
obj.person_info("wick",24)
obj.empployee_info(37000,"python")