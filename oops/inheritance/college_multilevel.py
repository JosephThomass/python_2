class College:
    def __init__(self):
        self.cname=""
        self.clocation=""
    def set_college(self):
        self.cname=input("Enter the college name :")
        self.clocation=input("Enter College location: ")
    def display_college(self):
        print("______________C_O_L_L_E_G_E___________")
        print("College name :",self.cname)
        print("College location : ",self.clocation)

class Department(College):
    def __init__(self):
        self.Department_name=""
        self.department_id=""
        self.department_head=""

    def set_department(self):
        obj.set_college()
        
        self.Department_name=input("Enter name of Depatrment: ")
        self.department_id=input("ID of department : ")
        self.department_head=input("Enter HOD name: ")
    def display_department(self):
        obj.display_college()
        print("_________D_E_P_A_R_T_M_E_N_T_________________")
        print("Department name :",self.Department_name)
        print("Department ID : ",self.department_id)
        print("Department head: ",self.department_head)

class Teacher(Department):
    def __init__(self):
        self.teacher_name=""
        self.subject=""

    def set_teacher(self):
        obj.set_department()
        self.teacher_name=input("Enter teacher name: ")
        self.subject=input("Enter the subject: ")
    def dispaly_teacher(self):
        obj.display_department()
        print("________T_E_A_C_H_E_R__________")
        print("Teacher name: ",self.teacher_name)
        print("Teacher's subject: ",self.subject)
    
class Student(Teacher):
    def __init__(self):
        self.student_name=""
        self.student_age=""
        self.student_mob=""
        self.student_course=""
        self.student_email=""

    def set_student(self):
        obj.set_teacher
        self.student_name=input("Enter Student name: ")
        self.student_age=input("Enter stuednt age: ")
        self.student_mob=input("Enter stuednt phone number :")
        self.student_course=input("Enter Course enroled :")
        self.student_email=input("Enter Email ID :")

    def display_student(self):
        obj.dispaly_teacher()
        print("______S_T_U_D_E_N_T_S_______")
        print("Name: ",self.student_name)
        print("Age: ",self.student_age)
        print("Mobile: ",self.student_mob)
        print("Course",self.student_course)
        print("Email: ",self.student_email)

obj=Student()
obj.set_student()
obj.display_student()

