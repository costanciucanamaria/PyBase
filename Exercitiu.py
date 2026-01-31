# 1. Creati o functie "top_students" care extrage toti studentii cu un test_score mai mare de 90, si returneaza o lista cu acei studenti.

# 2. Creaza o functie "extract_students" care extrage toti studentii "bachelor" si "masters", intr-un dictionar si il returneaza. Dictionarul arata in urmatorul fel:

example_dict = {
    "bachelor": [{"name": "Mason Dubois", "age": 21, "test_score": 71, "role": "bachelor"}, {"name": "Ethan Singh", "age": 20, "test_score": 79, "role": "bachelor"}],
    "masters": [{"name": "Isabella Nowak", "age": 25, "test_score": 89, "role": "masters"}, {"name": "Isabella Nowak", "age": 25, "test_score": 89, "role": "masters"}]
}

# 3. Creaza o functie "student_balance" care returneaza "bachelor" daca sunt mai multi bachelor decat masters, si "masters" daca sunt mai multi masters decat bachelor.

students = [
    {"name": "Emma Thompson", "age": 21, "test_score": 88, "role": "bachelor"},
    {"name": "Liam Chen", "age": 22, "test_score": 76, "role": "bachelor"},
    {"name": "Sofia Rodriguez", "age": 24, "test_score": 92, "role": "masters"},
    {"name": "Noah Patel", "age": 20, "test_score": 65, "role": "bachelor"},
    {"name": "Ava Müller", "age": 23, "test_score": 95, "role": "masters"},
    {"name": "Lucas Kim", "age": 19, "test_score": 82, "role": "bachelor"},
    {"name": "Isabella Nowak", "age": 25, "test_score": 89, "role": "masters"},
    {"name": "Mason Dubois", "age": 21, "test_score": 71, "role": "bachelor"},
    {"name": "Olivia Rossi", "age": 22, "test_score": 94, "role": "masters"},
    {"name": "Ethan Singh", "age": 20, "test_score": 79, "role": "bachelor"},
]

print("Exercitiu 1:")


def top_students(students):
    result = []
    for student in students:
        if student["test_score"] > 90:
            result.append(student["name"])
    return result

print(top_students(students))

print("Exercitiu 2:")

def extract_students(students):
   result = {
       "bachelor": [],
       "masters": []
   }
   for student in students:
       if student["role"] == "bachelor":
           result["bachelor"].append(student)
       elif student["role"] == "masters":
           result["masters"].append(student)
   return result

print(extract_students(students))

print("Exercitiu 3:")

def student_balance(students):
    bachelor = 0
    masters = 0
    for student in students:
        if student["role"] == "masters":
            bachelor += 1
        elif student["role"] == "bachelor":
            bachelor += 1
    if bachelor > masters:
        return "bachelor"
    elif masters > bachelor:
        return "masters"
    else:
        return "equal"

print(student_balance(students))

#C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\Exercitiu.py
#Exercitiu 1:
#['Sofia Rodriguez', 'Ava Müller', 'Olivia Rossi']
#Exercitiu 2:
#{'bachelor': [{'name': 'Emma Thompson', 'age': 21, 'test_score': 88, 'role': 'bachelor'}, {'name': 'Liam Chen', 'age': 22, 'test_score': 76, 'role': 'bachelor'}, {'name': 'Noah Patel', 'age': 20, 'test_score': 65, 'role': 'bachelor'}, {'name': 'Lucas Kim', 'age': 19, 'test_score': 82, 'role': 'bachelor'}, {'name': 'Mason Dubois', 'age': 21, 'test_score': 71, 'role': 'bachelor'}, {'name': 'Ethan Singh', 'age': 20, 'test_score': 79, 'role': 'bachelor'}], 'masters': [{'name': 'Sofia Rodriguez', 'age': 24, 'test_score': 92, 'role': 'masters'}, {'name': 'Ava Müller', 'age': 23, 'test_score': 95, 'role': 'masters'}, {'name': 'Isabella Nowak', 'age': 25, 'test_score': 89, 'role': 'masters'}, {'name': 'Olivia Rossi', 'age': 22, 'test_score': 94, 'role': 'masters'}]}
#Exercitiu 3:
#bachelor
#
#Process finished with exit code 0
