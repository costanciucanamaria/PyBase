from typing import Dict, List
# tipuri de date

# int, float, string, bool
print("==================Int======================")


def fc1(param1: int, param2: int = 10)-> int:
    param1 += 10
    return param1

print("Adunam 300 cu 10:")

var1 = 300
print(fc1(var1))

print("Adunam 30 cu 10 si 20:")

result = fc1(30)
result += 20
print(result)

var3 = 300
result = fc1(30)
result += 20
print(fc1(3.1))

#var1 = 300
#print(fc1("Hello"))

print("==================List======================")

def fc2(param1: List):
    return param1[0]

print(fc2([10, 20, 30]))

print("==================Classes======================")

class Hospital:
    def __init__(self):
        self.patients = []

    def recieve_patient(self, patient):
        self.patients.append(patient)

    def cure_patient(self, patient):
        for patient in self.patients:
            if patient.name == patient.name:
                #cure patient
                patient.is_sick = False

    #pacientul poate sa vorbeasca independent de spital.
    def ask_all_patients(self):
        for patient in self.patients:
            print(patient.talk())

    def get_patient_count(self):
        return len(self.patients)

    def __str__(self):
        return str(self.patients)


class Patient:
    def __init__(self, name, sickness, is_sick = True):
        self.name = name
        self.sickness = sickness
        self.is_sick = is_sick

    def talk(self):
        return f"Hi, my name is {self.name}, and I have {self.sickness}."

    def ask_hospital_how_many_patients_it_has(self, hospital):
        patients_count = hospital.get_patient_count()
        return f"I'm {self.name}, and I know the hospital has {patients_count} patients."

    def __str__(self):
        sickness_status = "not sick."
        if self.is_sick:
            sickness_status = "still sick. "
        return f"Patient: {self.name} with original sickness: {self.sickness} that is  {sickness_status}"

    def __repr__(self):
        return f"Patient('{self.name}', '{self.sickness}', {self.is_sick})"

p1 = Patient("Paul", "pneumonia")
p2 = Patient("Alina", "breast_cancer", False)
p3 = Patient("Vlad", "CFS")

h1 = Hospital()
h1.recieve_patient(p1)
h1.recieve_patient(p2)
h1.recieve_patient(p3)

h1.cure_patient("Paul")
h1.cure_patient("Vlad")

h1.ask_all_patients()

print(h1)
print(p1)
print(p3.talk())
print(h1.get_patient_count())
print(p3.ask_hospital_how_many_patients_it_has(h1))