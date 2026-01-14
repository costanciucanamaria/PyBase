# o variabila poate avea orice nume; poate fi un numar, un string sau o lista

# Tuplu
# in py e o structura de date imutabila, e ca un fel de lista, dar e fixa, neschimbabila.
# noi putem crea un tuplu, dar dupa aceeea nu putem schimba, sintaxa este sa fie intre paranteze rotunde;


persoana1 = ("Adrian", 32, "Brasov", "Tutore", 185, 70)
# Arian e pe pozitia 0, 1,   2,        3,       4,   5
# => Acestia sunt indecsii acestui tuplu
persoana2 = ("Ana-Maria", 35, "Lupeni", "Studenta", 157, 64)

print(coordonate_punct1)
print(coordonate_punct2)

print(persoana1)
print(persoana2)

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\01_data_structures.py
# ('Adrian', 32, 'Brasov', 'Tutore', 185, 70)
# ('Ana-Maria', 35, 'Lupeni', 'Studenta', 157, 64)
# Brasov
#
# Process finished with exit code 0

# nu pot crea o variabila True deoarece este o sintaxa de python; la fel si False;
# ctrl+space sa vad tot ce pot sa scriu
# cuvinte rezervate de python pentru chestii super specifice si cu ele nu putem crea variabile

# cum tuplul e ca o lista, are si index

# cum putem vedea orasul?

print(persoana1[2])
# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\01_data_structures.py
# Brasov
#
# Process finished with exit code 0

persoana1[3] = "Student"
print(persoana1[3])

# TypeError: 'tuple' object does not support item assignment


# lista
persoana3 = ["Noemi", 34, "Timisoara", "Student", 165, 50]

print(persoana3)

persoana3[3] = "Tutore"
print(persoana3[3])

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\01_data_structures.py
# ['Noemi', 34, 'Timisoara', 'Student', 165, 50]
# Tutore
#
# Process finished with exit code 0

# de observat ca in tuplu nu se schimba, dar in lista se schimba


tuplu2 = ("Tudor", (30, "Cluj", "Tamplar", ("Universitate", "Europa")))

print(tuplu2)

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\01_data_structures.py
# ('Tudor', (30, 'Cluj', 'Tamplar', ('Universitate', 'Europa')))
#
# Process finished with exit code 0


tuplu2 = ("Tudor", (30, "Cluj", "Tamplar", ("Universitate", "Europa", ("Sursa Divina", ("Pur Existenta")))))
#            0       1       2       3           4               5           6               7
# tuplu2[1]          0       1       2           3               4           5               6
# tuplu2[1][3]                                   0               1           2               3
# tuplu2[1][3][2]                                                            0               1

print(tuplu2[1][3][2][1])
# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\01_data_structures.py
# Pur Existenta
#
# Process finished with exit code 0

print(tuplu2[1][2])
# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\01_data_structures.py
# Tamplar
#
# Process finished with exit code 0


print(tuplu2[1][3])
# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\01_data_structures.py
# ('Universitate', 'Europa', ('Sursa Divina', 'Pur Existenta'))
#
# Process finished with exit code 0

print(tuplu2[1][3][2])
# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\01_data_structures.py
# ('Sursa Divina', 'Pur Existenta')
#
# Process finished with exit code 0


# tuplu2[1]          -> (30, "Cluj", "Tamplar", ("Universitate", "Europa",("Sursa Divina", ("Pur Existenta"))))
# tuplu2[1][3]       -> ("Universitate", "Europa",("Sursa Divina", ("Pur Existenta")))
# tuplu2[1][3][2]    -> ("Sursa Divina", ("Pur Existenta"))
# tuplu2[1][3][2][1] -> "Pur Existenta"

# legat de tupluri, vrem sa tinem datele impreuna; e mai rar folosit in python

# SETS

# un set in mate e o grupare de elemente unice

# {3, 4, 100, 200, 5, 9, 0}
# {}

# nu este set: {3, 4, 3} - un set are doar elemente unice

var2 = {3, 4, 10, 0}
print(var2)

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\01_data_structures.py
# {0, 10, 3, 4}
#
# Process finished with exit code 0

# => Python mi-a dat alta ordine, stie doar ca sunt unice elementele, nu stie ca au ordine

var2 = {3, 4, 10, 0}

var2.add(100)  # se adauga 100
print(var2)

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\01_data_structures.py
# {0, 3, 100, 4, 10}
#
# Process finished with exit code 0

var2 = {3, 4, 10, 0}

var2.add(100)
var2.remove(10)  # se scoate 10

print(var2)

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\01_data_structures.py
# {0, 3, 100, 4}
#
# Process finished with exit code 0

persoane = ["Tudor", "Maria", "Vlad", "Marius", "Adrian", "Flavia", "Vlad"]
print(persoane)

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\01_data_structures.py
# ['Tudor', 'Maria', 'Vlad', 'Marius', 'Adrian', 'Flavia', 'Vlad']
#
# Process finished with exit code 0

var4 = set(persoane)
print(var4)

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\01_data_structures.py
# {'Maria', 'Flavia', 'Marius', 'Adrian', 'Tudor', 'Vlad'}
#
# Process finished with exit code 0


if "Marius" in persoane:
    print("Marius este printre noi.")
else:
    print("Marius nu este printre noi.")

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\01_data_structures.py
# Marius este printre noi.
#
# Process finished with exit code 0


persoane = ["Tudor", "Maria", "Vlad", "Popa", "Adrian", "Flavia", "Vlad"]

if "Marius" in persoane:
    print("Marius este printre noi.")
else:
    print("Marius nu este printre noi.")

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\01_data_structures.py
# Marius nu este printre noi.
#
# Process finished with exit code 0


persoane = ["Tudor", "Maria", "Vlad", "Adrian", "Flavia", "Vlad", "Marius"]  # Marius e pe ultimul loc acum

var4 = set(persoane)

# 7 pasi, s-a uitat la fiecare element pana a ajuns la Marius
# complexitatea codului este O(n) - la noi n este 7 -> Complexitate liniara ; daca in loc de 7 era 1 miliard, se uita la un miliard de elemente

if "Marius" in persoane:
    print("Marius este printre noi.")
else:
    print("Marius nu este printre noi.")

# 1 pas
# complexitatea este O(1) -> Constant
# orice element din set primeste un hash (2309458034875956734453), iar fiecare hash este unic  - se intampla in mai putin de o milisecunda
# pentru  ca nu e ordonat, adaugarea si stergerea la fel se intampla instant


if "Marius" in var4:
    print("Marius este printre noi.")
else:
    print("Marius nu este printre noi.")

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\01_data_structures.py
# Marius este printre noi.
# Marius este printre noi.
#
# Process finished with exit code 0


# Liste si stringuri

# un string este un sir de caractere

str1 = "LOG: Hello this is Vlad the Impaler."
str2 = "WARN: My story is overblown."
str3 = "ERROR: !@#$%^&*()_____{}:"

list3 = ["adrian", "client", "studenti"]
list4 = [str1, str2, str3]

print(list4)
# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\01_data_structures.py
# ['LOG: Hello this is Vlad the Impaler.', 'WARN: My story is overblown.', 'ERROR: !@#$%^&*()_____{}:']
#
# Process finished with exit code 0

# task: split all the strings in our list, split them using the ":" character
# example: "LOG: Hello this is Vlad the Impaler." -> ["LOG", "Hello this is Vlad the Impaler."]


print(list4[0])

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\01_data_structures.py
# LOG: Hello this is Vlad the Impaler.
#
# Process finished with exit code 0


print(list4[0].split(":"))

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\01_data_structures.py
# ['LOG', ' Hello this is Vlad the Impaler.']
#
# Process finished with exit code 0


print(list4[0].split(":"))
print(list4[1].split(":"))
print(list4[2].split(":"))

# => Asa merge, dar aceasta metoda este manuala

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\01_data_structures.py
# ['LOG', ' Hello this is Vlad the Impaler.']
# ['WARN', ' My story is overblown.']
# ['ERROR', ' !@#$%^&*()_____{}', '']
#
# Process finished with exit code 0

print(list(range(10)))

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\01_data_structures.py
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Process finished with exit code 0

print(list(range(100)))

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\01_data_structures.py
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
#
# Process finished with exit code 0

print(list(range(1000000000)))
# MemoryError

print(len(list4))
print(list(range(len(list4))))

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\01_data_structures.py
# 3
# [0, 1, 2]
#
# Process finished with exit code 0


for i in range(10):
    print(i)

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\01_data_structures.py
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
#
# Process finished with exit code 0

for i in range(len(list4)):
    print(i)

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\01_data_structures.py
# 0
# 1
# 2
#
# Process finished with exit code 0


for i in range(len(list4)):
    print(list4[i])

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\01_data_structures.py
# LOG: Hello this is Vlad the Impaler.
# WARN: My story is overblown.
# ERROR: !@#$%^&*()_____{}:
#
# Process finished with exit code 0


print("==========")
list5 = [10, 20, 30]
list5[1] = 100
print(list5)

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\01_data_structures.py
# LOG: Hello this is Vlad the Impaler.
# WARN: My story is overblown.
# ERROR: !@#$%^&*()_____{}:
# ==========
# [10, 100, 30]
#
# Process finished with exit code 0

for i in range(len(list4)):
    list4[i] = list4[i].split(":")
print(list4)

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\01_data_structures.py
# [['LOG', ' Hello this is Vlad the Impaler.'], ['WARN', ' My story is overblown.'], ['ERROR', ' !@#$%^&*()_____{}', '']]
#
# Process finished with exit code 0

# se poate compara

print(list4)
# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\01_data_structures.py
# ['LOG: Hello this is Vlad the Impaler.', 'WARN: My story is overblown.', 'ERROR: !@#$%^&*()_____{}:']
#
# Process finished with exit code 0