class Hospital:
    def __init__(self):
        self.hospital_name=""
        self.place=""
    def set_hospital(self):
        self.hospital_name=input("Enter Hospitl name : ")
        self.place=input("Enter hospital location :")

    def display_hospital(self):
        print("$ $ $ HOSPITAL DETAILS $ $ $")
        print("Hospital name is ",self.hospital_name)
        print("Hospital Location is : ",self.place)
        print()


class PatientSection(Hospital):
    def __init__(self):
        self.section_name=""
        self.doctor=""

    def set_department(self):
        obj.set_hospital()
        self.section_name=input("Enter Section name : ")
        self.doctor=input("Enter Doctors name :")

    def display_section(self):
        obj.display_hospital()
        print("$ $ $ Department Details $ $ $ ")
        print("section :",self.section_name)
        print("Doctor : ",self.doctor)
        print()

class Patient(PatientSection):
    def __init__(self):
        self.patient_name=""
        self.age=""
        self.mobile=""
        self.location=""
    def set_patient(self):
        obj.set_department()
        self.patient_name=input("Enter patient name: ")
        self.age=input("Enter patient's age: ")
        self.mobile=input("Enter patient mobile nnumber: ")
        self.location=input("Enterr patient location: ")
    def display_patient(self):
        obj.display_section()
        print("$ $ $ patient details $ $ $ ")
        print("Patient name: ",self.patient_name)
        print("Patient age : ",self.age)
        print("Patient mobile :", self.mobile)
        print("Patient location : ",self.location)
        print()
obj=Patient()
obj.set_patient()
obj.display_patient()