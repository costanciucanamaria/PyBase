import copy

from operators_strings import rezultat

# acest import se uita intr-un pachet py din libraria standard si poate sa importe acest modul

print("====================pass by value==========================")

var1 = "hello"

def change_variable(param1):
    param1 = "this is not a hello."

print(var1)
# pass by value (aici nu se schimba)
change_variable(var1)
print(var1)

print("====================pass by reference==========================")

var2 = [30, 100]

def change_variable_list(param1):
    param1.append(99)
    param1.clear() # a sters toate elementele din lista

print(var2)
# pass by reference (aici se schimba)
change_variable_list(var2)
print(var2)

print("====================max si suma nr dintr-o lista==========================")

lista2 = [40, 90, 100, 10, 4, 1]

total = 0

print("====================ne printeaza toate elementele din lista==========================")

for nr in lista2:
    print(nr)

print("====================total==========================")

# pot sa iau acest cod si sa il bag intr-o functie:

for nr in lista2:
    total = total + nr

print(total)

print("====================total in functie==========================")


def get_total(param1):
    total = 0
    for nr in param1:
        total = total + nr
    return total

print(get_total(lista2))

print("====================max==========================")

# cum calculam un max in capul nostru: 40 < 90 < 100 > 10 > 4 > 1

max = lista2[0]

for nr in lista2:
    if nr > max:
        max = nr

print(max)

print("====================in functie==========================")

def get_max(param1):
    max = param1[0]
    for nr in param1:
        if nr > max:
            max = nr
    return max

print(get_max(lista2))

print("=============================================dictionare==================================================")
print("=========================================================================================================")
print("=========================================================================================================")
print("=========================================================================================================")


# un dictionar e tot ca un fel de lista, dar perechile din dictionar sunt chei valoare
# un dictionar e definit prin acolade
# cele mai folosoite structuri de date, super generic
# un dictionar poate avea o singura cheie cu numele acesta: age (sau cnp, name, weight, profession, fav_food, backpack)
# fiecarei chei i se genereaza un hash
# nu accepta lista (1, 2) deoarece se poate schimba

# key             value
# cnp             2907765567545
# name            Adrian
# age             32
# weight          70
# profession      programmer
# fav_food        pasta
# backpack        [keys, wallet, camera, phone]


student = {
    "name": "Adrian",
    "age": 32,
    "weight": 70.0,
    "backpack": ["keys", "wallet", "camera", "phone"]
}

print(student)
print("====================student name==========================")
print(student["name"])
print("====================student backpack==========================")
print(student["backpack"])
print("====================student backpack - ceva din lista==========================")
print(student["backpack"][2])

print("====================cheile din dictionar==========================")

student.keys()

for k in student.keys():
    print(k)

print("====================valorile din dictionar==========================")
for v in student.values():
    print(v)

print("====================keys and values==========================")

for key, value in student.items():
    print(key, "----", value)

print("====================ce se mai accepta in dictionare==========================")

student = {
    "name": "Adrian",
    "age": 32,
    "weight": 70.0,
    "backpack": ["keys", "wallet", "camera", "phone"],
    0: "nothing at all",
    (1,2): "alpha and omega" # se accepta si tupluri
}

print("====================se poate schimba valoarea==========================")

print(student)
print("====================se poate schimba varsta==========================")

student["age"] = 33
print(student)

print("====================se poate adauga adresa==========================")
student["address"] = "Brasov"
print(student)

print("====================get==========================")
# daca nu stim toate cheile
print("====================daca nu exista cheia==========================")

print(student.get("hhhh"))
print("====================daca nu exista cheia si daca pui o valoare==========================")
print(student.get("hhhh", "default value"))
print("====================daca pun cheia care lipsea nu mai apare default value==========================")

student["hhhh"] = "assassin"
print(student.get("hhhh", "default value"))

print("====================se poate sterge o cheie==========================")
student.pop("address")
print(student)

if "address" in student:
    print("Avem adresa pentru student!")
else:
    print("Studentul acesta nu are adresa!")

print("====================se adauga student 2==========================")

student_doi = student
student_doi["restante"] = 3
print("Student original:")
print(student_doi)

print("====================se printeaza student original==========================")
print(student)

print("====================se face clona==========================")
student_doi = student.copy()
student_doi["restante"] = 3
print("Student original:")
print(student)
print("====================shallow copy drawbacks==========================")
student_doi["backpack"].append("casti")
print(student_doi)
print(student)

print("====================deep copy==========================")
student_trei = copy.deepcopy(student)
student_trei["backpack"].append("umbrela")

print(student_trei)
print("Student original:")
print(student)

print("====================Function dict exercises================================")
print("====================cum aflu ca e numar================================")
print("====================30 ================================")

var4 = 30
print(isinstance(var4, int)) #true
print(isinstance(var4, float)) #false

print("====================30.4 ================================")
var5 = 30.4
print(isinstance(var5, int)) #false
print(isinstance(var5, float)) #true

var6 = "100"
print(isinstance(var5, int)) #false
print(isinstance(var5, float)) #true
print("====================creeaza o functie care aduna toate numerele din dictionar:================================")

dict2 = {
    "name": "Omega",
    "dimensions": 6,
    "size": 13,
    "count": -1,
    "axis": "y",
    "trees": "all"
}
# cum le putem aduna?

def add_all_numbers(param1):
    total = 0
    # sa aflam care sunt numere; trecem prin toate cheile si care sunt numere le adunam
    for key in dict2.keys():
        valoarea = dict2[key]
        if isinstance(valoarea, int):
            total = total + valoarea
    return total

print(add_all_numbers(dict2))

print("====================Odd/Even Numbers ================================")

# 5 / 2 -> 2, rest 1

print("====================ac impartire ne da restul ================================")

print(5 % 2) #1
print(17 % 2) # 1



is_even(5) #False
is_even(10) #True

print("====================vrem sa adunam toate numerele pare ================================")

def is_even(nr):
    return nr % 2 == 0 # aici este restul


lista3 = [5, 10, 4, 30, 25, 7]


def add_all_evens(param1):
    total = 0
    # sa aflam care sunt numere pare; trecem prin toate cheile si care sunt numere pare le adunam
    for nr in param1:
        if is_even(nr):
            total = total + nr
    return total

rezultat = add_all_evens(lista3)
print(rezultat)



#C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\05_functions.py
#120
#120
#242
#726
#8
#734
#3
#1
#5
#8
#81
#True
#False
#0
#True
#True
#False
#42
#0b101010
#0x2a
#0b111
#0b10
#0b100
#Hello World!
#Hello World!
#<class 'str'>
#<class 'str'>
#
#a
#a
#97
#A
#65
#97
#S
#$
#Primul rand Al doilea rand Al treilea rand
#Primul rand
#Al doilea rand
#Al treilea rand
#Primul rand
#Al doilea rand
#Al treilea rand
#Test VoltageCheck finished in 1.23
#Test VoltageCheck finished in 2.24
#Test VoltageCheck finished in 2.2379
#VOLTAGECHECK
#====================pass by value==========================
#hello
#hello
#====================pass by reference==========================
#[30, 100]
#[]
#====================max si suma nr dintr-o lista==========================
#====================ne printeaza toate elementele din lista==========================
#40
#90
#100
#10
#4
#1
#====================total==========================
#245
#====================total in functie==========================
#245
#====================max==========================
#100
#====================in functie==========================
#100
#=============================================dictionare==================================================
#=========================================================================================================
#=========================================================================================================
#=========================================================================================================
#{'name': 'Adrian', 'age': 32, 'weight': 70.0, 'backpack': ['keys', 'wallet', 'camera', 'phone']}
#====================student name==========================
#Adrian
#====================student backpack==========================
#['keys', 'wallet', 'camera', 'phone']
#====================student backpack - ceva din lista==========================
#camera
#====================cheile din dictionar==========================
#name
#age
#weight
#backpack
#====================valorile din dictionar==========================
#Adrian
#32
#70.0
#['keys', 'wallet', 'camera', 'phone']
#====================keys and values==========================
#name ---- Adrian
#age ---- 32
#weight ---- 70.0
#backpack ---- ['keys', 'wallet', 'camera', 'phone']
#====================ce se mai accepta in dictionare==========================
#====================se poate schimba valoarea==========================
#{'name': 'Adrian', 'age': 32, 'weight': 70.0, 'backpack': ['keys', 'wallet', 'camera', 'phone'], 0: 'nothing at all', (1, 2): 'alpha and omega'}
#====================se poate schimba varsta==========================
#{'name': 'Adrian', 'age': 33, 'weight': 70.0, 'backpack': ['keys', 'wallet', 'camera', 'phone'], 0: 'nothing at all', (1, 2): 'alpha and omega'}
#====================se poate adauga adresa==========================
#{'name': 'Adrian', 'age': 33, 'weight': 70.0, 'backpack': ['keys', 'wallet', 'camera', 'phone'], 0: 'nothing at all', (1, 2): 'alpha and omega', 'address': 'Brasov'}
#====================get==========================
#====================daca nu exista cheia==========================
#None
#====================daca nu exista cheia si daca pui o valoare==========================
#default value
#====================daca pun cheia care lipsea nu mai apare default value==========================
#assassin
#====================se poate sterge o cheie==========================
#{'name': 'Adrian', 'age': 33, 'weight': 70.0, 'backpack': ['keys', 'wallet', 'camera', 'phone'], 0: 'nothing at all', (1, 2): 'alpha and omega', 'hhhh': 'assassin'}
#Studentul acesta nu are adresa!
#====================se adauga student 2==========================
#Student original:
#{'name': 'Adrian', 'age': 33, 'weight': 70.0, 'backpack': ['keys', 'wallet', 'camera', 'phone'], 0: 'nothing at all', (1, 2): 'alpha and omega', 'hhhh': 'assassin', 'restante': 3}
#====================se printeaza student original==========================
#{'name': 'Adrian', 'age': 33, 'weight': 70.0, 'backpack': ['keys', 'wallet', 'camera', 'phone'], 0: 'nothing at all', (1, 2): 'alpha and omega', 'hhhh': 'assassin', 'restante': 3}
#====================se face clona==========================
#Student original:
#{'name': 'Adrian', 'age': 33, 'weight': 70.0, 'backpack': ['keys', 'wallet', 'camera', 'phone'], 0: 'nothing at all', (1, 2): 'alpha and omega', 'hhhh': 'assassin', 'restante': 3}
#====================shallow copy drawbacks==========================
#{'name': 'Adrian', 'age': 33, 'weight': 70.0, 'backpack': ['keys', 'wallet', 'camera', 'phone', 'casti'], 0: 'nothing at all', (1, 2): 'alpha and omega', 'hhhh': 'assassin', 'restante': 3}
#{'name': 'Adrian', 'age': 33, 'weight': 70.0, 'backpack': ['keys', 'wallet', 'camera', 'phone', 'casti'], 0: 'nothing at all', (1, 2): 'alpha and omega', 'hhhh': 'assassin', 'restante': 3}
#====================deep copy==========================
#{'name': 'Adrian', 'age': 33, 'weight': 70.0, 'backpack': ['keys', 'wallet', 'camera', 'phone', 'casti', 'umbrela'], 0: 'nothing at all', (1, 2): 'alpha and omega', 'hhhh': 'assassin', 'restante': 3}
#Student original:
#{'name': 'Adrian', 'age': 33, 'weight': 70.0, 'backpack': ['keys', 'wallet', 'camera', 'phone', 'casti'], 0: 'nothing at all', (1, 2): 'alpha and omega', 'hhhh': 'assassin', 'restante': 3}
#====================Function dict exercises================================
#====================cum aflu ca e numar================================
#====================30 ================================
#True
#False
#====================30.4 ================================
#False
#True
#False
#True
#====================creeaza o functie care aduna toate numerele din dictionar:================================
#18
#====================Odd/Even Numbers ================================
#====================ac impartire ne da restul ================================
#1
#1
#====================vrem sa adunam toate numerele pare ================================
#44
#
#Process finished with exit code 0