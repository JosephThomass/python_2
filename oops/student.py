class Student:
    def __init__(self,name,rollno,department,emailid,phonenumber,):
        self.departme=department
        self.sname=name
        self.smob=phonenumber
        self.semail=emailid
        self.rollnumber=rollno
    def displaydata(self):
        print(f'name: {self.sname}')
        print(f'Roll no: {self.rollnumber}')
        print(f"Phone Number: {self.smob}")
        print(f"Email ID : {self.semail}")
        print(f"Department :{self.departme}")
std1=Student("Amal",27,"CSE","Amalcse23@gmail.com",8086116165)
std2=Student("Emil",15,"Civil","emil@yahoomail.com",9995558887)
std1.displaydata()
std2.displaydata()