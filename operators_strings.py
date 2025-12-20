# Tipuri de string
#protocoale de comunicatie; ethernet se foloseste http; fiecare protocol are un set de reguli, a.i. sa fie inteleasa partea de trimitere si de receptie;
#alta varianta:

produs = 1

for i in range(5):
    produs = produs * (i+1)

print(produs)

import math

produs = math.factorial(5)

print(produs)

#Doimea unui numar este 121. Afla triplul numarului, la care adaugam produsul numerelor pare mai mici decat 6, diferite de 0.

doimea_nr = 121
nr = doimea_nr * 2
triplu_nr = nr * 3
produs_numere_pare = 1
#trebuie sa il exclud pe 0 si sa filtrez doar numerele pare
for i in range(6):
    if i % 2 == 0 and i!=0:
        produs_numere_pare = produs_numere_pare * i

rezultat = triplu_nr + produs_numere_pare

print(nr)
print(triplu_nr)
print(produs_numere_pare)
print(rezultat)


#C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\operators_strings.py
#242
#726
#8
#734
#
#Process finished with exit code 0


# Operatorul // este o impartire cu rest; rezultatul este catul impartirii;

a = 10
b = 3

# pentru cat
imp_cat = a // b
print (imp_cat)

# pentru rest
cat = a % b
print (cat)

# exercitiu

boxes = 53
boxes_per_pallet = 10

full_pallets = boxes // boxes_per_pallet
print (full_pallets)

#C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\operators_strings.py
#3
#1
#5
#
#Process finished with exit code 0

# ** - Puterea unui numar

a = 2
b = 3

c = a**b

print(c)

#C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\operators_strings.py
#8
#
#Process finished with exit code 0

# ex realitate

modes = 3
devices = 4

# fiecare device functioneaza in 3 moduri diferite
# care e numarul total de combinatii pt device-urile mele

combin = modes ** devices
print(combin)

#C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\operators_strings.py
#81
#
#Process finished with exit code 0

# o masina care are usa deschisa si porneste doar daca are usa inchisa, iar butonul de emergency stop nu este apasat
# trebuie sa implementam acest algoritm si sa ne asiguram ca doar in aceste conditii poate sa porneasca masina

door_closed = True
emergency_stop_pressed = False

start_machine = door_closed and not emergency_stop_pressed

print(start_machine)

#C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\operators_strings.py
#True
#
#Process finished with exit code 0

door_closed = False
emergency_stop_pressed = False

start_machine = door_closed and not emergency_stop_pressed

print(start_machine)

#C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\operators_strings.py
#False
#
#Process finished with exit code 0

#se poate folosi si int

door_closed = 0
emergency_stop_pressed = 1

start_machine = door_closed and not emergency_stop_pressed

print(start_machine)

#C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\operators_strings.py
#False
#0
#
#Process finished with exit code 0

#este indicat sa folosim totusi boolean!

# putem pune cate conditii dorim:

door_closed = True
emergency_stop_pressed = False
breaks_pressed = True

start_machine = door_closed and not emergency_stop_pressed and breaks_pressed


print(start_machine)


#C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\operators_strings.py
#True
#
#Process finished with exit code 0

# am de facut un test pt un device;
# # trb sa vad daca e passed sau failed;
# daca presiunea este ok si comunicatia cu alte device-uri este ok;


voltage_ok = True
communication_ok = False

test_failed = (not voltage_ok) or (not communication_ok)
#am folosit parantezele pentru a fi mai ok dpdv vizual

print(test_failed)

#C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\operators_strings.py
#True
#
#Process finished with exit code 0

voltage_ok = True
communication_ok = True

test_failed = (not voltage_ok) or (not communication_ok)

print(test_failed)

#C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\operators_strings.py
#False
#
#Process finished with exit code 0


# operatori pe biti (bitwise)
# reprezentarea numerelor in decimal, binar sau hexadecimal

#am declarat aceasta valoare care este un int
value = 42

#am printat valoarea valoarea decimala
print(value)

#am printat reprezentarea binara
print(bin(value))

#am printat reprezentarea hexa - se foloseste 0x
print(hex(value))

#C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\operators_strings.py
#decimal: 42
#binar: 0b101010
#hexa: 0x2a
#
#Process finished with exit code 0


# | - Operator sau pe biti
# & - Operator si  pe biti
# ~ - Operator not pe biti

# sa fac un sistem in care sa acord permisiuni de read, write sau execute

READ = 0b001
WRITE = 0b010
EXEC = 0b100

#Am codificat actiunile mele pri aceasta executie in binar
#la origine sunt variabile, dar fiind scrise cu litere mari le consideram constante si nu avem voie sa le alteram valoarea

user_permissions = READ | WRITE | EXEC

print(bin(user_permissions))

can_write = user_permissions & WRITE

print(bin(can_write))

can_exec = user_permissions & EXEC

print(bin(can_exec))

#C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\operators_strings.py
#0b111
#0b10
#0b100
#
#Process finished with exit code 0

# DE APROFUNDAT NOTIUNILE ACESTEA DE BINARI SI HEXA!!!!!!!!!

# Siruri de caractere sau stringuri
# stringurile sunt tipuri de date

print('Hello World!')

s = 'Hello World!'

print(s)

print(type(s))

my_string = ''
print(type(my_string))

print(my_string)

my_string1 = 'a'

print(my_string1)


#C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\operators_strings.py
#print('Hello World!'): Hello World!
#print(s): Hello World!
#print(type(s)): <class 'str'>
#print(type(my_string)): <class 'str'>
#print(my_string):                  aici trebuie sa fie gol
#print(my_string1): a
#
#Process finished with exit code 0


#cod ascii - de cautat pe Google
#fiecarui caracter ii assigneaza un numar

my_string = 'a'

print(my_string)

print(ord(my_string))

my_string1 = 'A'

print(my_string1)

print(ord(my_string1))

print(ord('a'))

print(chr(83)) #aici este invers

print(chr(36))

#C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\operators_strings.py
#a
#97
#A
#65
#97
#S
#$
#
#Process finished with exit code 0

#formatare
#primul rand
#al doilea rand
#al treilea rand

print('Primul rand Al doilea rand Al treilea rand')
print('Primul rand\nAl doilea rand\nAl treilea rand')
print('''Primul rand
Al doilea rand
Al treilea rand'''
)

#C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\operators_strings.py
#Primul rand Al doilea rand Al treilea rand
#Primul rand
#Al doilea rand
#Al treilea rand
##Primul rand
#Al doilea rand
#Al treilea rand
#
#Process finished with exit code 0


#ex logare de test results
#am niste rezultate de test si vreau sa le stochez undeva

test_name = 'VoltageCheck'
duration = 2.23789

#vreau sa imi afiseze Test, VoltageCheck finished in 1.23

#folosesc un concept de formatare a stringului

print('Test VoltageCheck finished in 1.23')
print(f'Test {test_name} finished in {duration:.2f}')
print(f'Test {test_name} finished in {duration:.4f}')


print(test_name.upper()) #data viitoare aprofundam partea asta

#C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\operators_strings.py
#Test VoltageCheck finished in 1.23
#Test VoltageCheck finished in 2.24
#Test VoltageCheck finished in 2.2379
#VOLTAGECHECK
#
#Process finished with exit code 0

#data viitoare incepem sa lucram la proiect
#data viitoare primim tema
#data viitoare facem lista