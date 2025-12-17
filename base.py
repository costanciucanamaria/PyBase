# in pycharm
cowsay.cow('Good Mooooorning!')
# nu va merge

# ------------------------
# in python console nu merge, DOAR in terminal:

# PyDev console: starting.
# Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
# pip install cowsay
#  File "<input>", line 1
#    pip install cowsay
#        ^^^^^^^
# SyntaxError: invalid syntax


# se merge la terminal

# (.venv) PS C:\playground\PyBase> pip install cowsay
# Collecting cowsay
#  Downloading cowsay-6.1-py3-none-any.whl.metadata (5.6 kB)
# Downloading cowsay-6.1-py3-none-any.whl (25 kB)
# Installing collected packages: cowsay
# Successfully installed cowsay-6.1
#
# [notice] A new release of pip is available: 25.1.1 -> 25.3
# [notice] To update, run: python.exe -m pip install --upgrade pip
# (.venv) PS C:\playground\PyBase>

# dupa aceea va merge
# -----------------------------------------------------------------------------------------
# command prompt
# Microsoft Windows [Version 10.0.19045.6466]
# (c) Microsoft Corporation. All rights reserved.
#
# C:\Users\LocalAccount>cd ..
#
# C:\Users>cd ..
#
# C:\>cd playground
#
# C:\playground>cd PyBase
#
# C:\playground\PyBase>python.exe hello.py
# Traceback (most recent call last):
#  File "C:\playground\PyBase\hello.py", line 1, in <module>
#    import cowsay
# ModuleNotFoundError: No module named 'cowsay'
#
# C:\playground\PyBase>dir
# Volume in drive C has no label.
# Volume Serial Number is 3A23-C2CF
#
# Directory of C:\playground\PyBase

# 12/17/2025  07:06 PM    <DIR>          .
# 12/17/2025  07:06 PM    <DIR>          ..
# 12/17/2025  07:08 PM    <DIR>          .idea
# 12/17/2025  06:47 PM    <DIR>          .venv
# 12/17/2025  06:49 PM                 0 base.py
# 12/17/2025  07:06 PM                96 hello.py
#               2 File(s)             96 bytes
#               4 Dir(s)  132,143,009,792 bytes free
#
# C:\playground\PyBase>cd .venv
#
# C:\playground\PyBase\.venv>cd scripts
#
# C:\playground\PyBase\.venv\Scripts>activate
#
# (.venv) C:\playground\PyBase\.venv\Scripts>..
# '..' is not recognized as an internal or external command,
# operable program or batch file.
#
# (.venv) C:\playground\PyBase\.venv\Scripts>cd ..
#
# (.venv) C:\playground\PyBase\.venv>cd ..
#
# (.venv) C:\playground\PyBase>python.exe hello.py
#  _________________
# | Good Mooooorning! |
#  =================
#                 \
#                  \
#                    ^__^
#                    (oo)\_______
#                    (__)\       )\/\
#                        ||----w |
#                        ||     ||
#
# (.venv) C:\playground\PyBase>deactivate
# C:\playground\PyBase>
#
# ------------------------------------------
# Debugging
# for, if, while, switch

a = 3
b = 6

c = b + a
print(c)

# avem numere naturale consecutive de la 1 la 10 (porneste de la 0 si se opreste la 9)
# avem un contor care isi mareste valoarea la fiecare iteratie
# pana ajungem la 10
# incepe de la 0 si ajunge pana la 9
# bucla se termina la valoarea care a fost pusa mai jos

# this is a for statement
for i in range(10):
    print(i)  # este nevoie de indentare la print. daca nu o avem, vom primi mesajul ca acest for nu este corect;
    print(2 * i)

# rezulate:
# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\base.py
# 9
# 0
# 0
# 1
# 2
# 2
# 4
# 3
# 6
# 4
# 8
# 5
# 10
# 6
# 12
# 7
# 14
# 8
# 16
# 9
# 18
#
# Process finished with exit code 0
# pe cifrele de la randuri se poate pune o bulina rosie
# se poate folosi butonul step over (dupa ||)

# pentru a pune doua operatii pe o linie avem nevoie de ;

for i in range(10):
    print(i)  # este nevoie de indentare la print. daca nu o avem, vom primi mesajul ca acest for nu este corect;
print(2 * i)

# rezultate:
# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\base.py
# 9
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
# 18
#
# Process finished with exit code 0

# TREBUIE SA FIM FOARTE ATENTI LA INDENTARE!!!!!!!!!!!!!!!!!!!!

# In alte limbaje de programare se folosesc acolade pentru acest for (ex: C). Python foloseste indentarea.

a = 3;
b = 6

c = b + a
# print(c)

# this is a for statement

# suma de la 1 la 10
# 1+2+3+4+...+10 daca nu as fi programator

suma = 0

for i in range(10):
    suma = suma + 1

print(suma)

# ar trebui sa fie 45, mie imi da 10

a = 3;
b = 6

c = b + a
# print(c)

# this is a for statement

# suma de la 1 la 10
# 1+2+3+4+...+10 daca nu as fi programator

suma = 0

for i in range(10):
    suma = suma + i

print(suma)

# acum da 45

# alta modalitate de a calcula numerele consecutive

suma1 = 0

for i in range(10):
    suma1 = suma1 + i

print(suma1)

# suma = n(n+1)/2

suma2 = 9 * (9 + 1) / 2
print(suma2)

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\base.py
# 45
# 45.0
#
# Process finished with exit code 0


# produs = 1*2*3*4*...*9

suma1 = 0
produs = 1

for i in range(10):
    suma1 = suma1 + i
    produs = produs * i
print(suma1)

# suma = n(n+1)/2

# suma2 = 9*(9+1)/2
# print (suma2)

print(produs)

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\base.py
# 45
# 0
#
# Process finished with exit code 0

# produs = 1*2*3*4*...*9

suma1 = 0
produs = 1

for i in range(3):
    suma1 = suma1 + i
    produs = produs * (i + 1)
print(suma1)

# suma = n(n+1)/2

# suma2 = 9*(9+1)/2
# print (suma2)

print(produs)

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\base.py
# 3
# 6
#
# Process finished with exit code 0

# produs = 1*2*3*4*...*9

suma1 = 0
produs = 1

for i in range(5):
    suma1 = suma1 + i
    produs = produs * (i + 1)
print(suma1)

# suma = n(n+1)/2

# suma2 = 9*(9+1)/2
# print (suma2)

print(produs)

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\base.py
# 10
# 120
#
# Process finished with exit code 0

# produs = 1*2*3*4*...*9

suma1 = 0
produs = 1

for i in range(10):
    suma1 = suma1 + i
    produs = produs * (i + 1)
print(suma1)

# suma = n(n+1)/2

# suma2 = 9*(9+1)/2
# print (suma2)

print(produs)

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\base.py
# 45
# 3628800
#
# Process finished with exit code 0


# tipuri de date
# folosite pentru numere:
int
float  # decimale

# produs = 1*2*3*4*...*9

suma1 = 0
produs = 1

for i in range(10):
    suma1 = suma1 + i
    produs = produs * (i + 1)
print(suma1)

# suma = n(n+1)/2

suma2 = 9 * (9 + 1) / 2
print(suma2)

print(produs)

print(type(suma2))

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\base.py
# 45
# 45.0
# 3628800
# <class 'float'>
#
# Process finished with exit code 0


# ce inseamna variabile?
# in programare o variabila este o notiune fundamentala pe care se bazeaza ff multe chestii mai complexe si alaturi de instructiuni si operatori constituie fundamentul cel mai de jos al programarii
# ex viata reala: un sertar din easybox
# dulapul mare e memoria ram a calculatorului, aici se stocheaza diferite variable
# o variabila poate avea nevoie de una sau mai multe locatii a memoriei
# fiecare sertar are o adrea unica
# in fiecare moment trb sa stiu la ce adresa merg pt a interoga o memorie

a = 3
print(id(a))

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\base.py
# 140718950360248
# Process finished with exit code 0

a = 3
a = 7
print(a)
print(id(a))

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\base.py
# 7
# 140718950360376
# Process finished with exit code 0


a = 3

aux = 55

a = aux
print(a)
print(id(a))

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\base.py
# 55
# 140718950361912
# Process finished with exit code 0


a = 3

aux = 55

a = aux * 5
print(a)
print(id(a))

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\base.py
# 275
# 1657763948464
# Process finished with exit code 0

# constanta e o variabila careia nu i se poate modifica valoarea
# in python nu exista optiunea de constanta la acest mod

PI = 3.14159

# in comunicarea dintre 2 device-uri e un schimb de mesaje
# daca nu primeste un raspuns la request, face ceva
# nu poate astepta la nesfarsit, are un timeout

TIMEOUT_MSG_X = 500  # In codul meu nu am voie sa modific asta

# numele variabilelor sa fie cat mai sugestive
suma_doua_numere = 0
check_flag = False
print(type(check_flag))
<

class 'bool'>
# conventii: nu se scriu cu litere mari, nu se scriu legate (checkFlag)
# nu pot incepe o variabila cu o cifra 6check
# daca pun _6check_flag e ok

# limbajul Python este case sensitive


Example = 1
example = 2

# 2 variabile diferite

example = 2

example += 3

print(example)

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\base.py
# 5
# Process finished with exit code 0

example = 2

# example += 3
example = example + 3

print(example)

C:\playground\PyBase\.venv\Scripts\python.exe
C:\playground\PyBase\base.py
5
Process
finished
with exit code 0

example = 2

# example += 3
example = example + 3

example = example + 1

# example += 1

print(example)

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\base.py
# 6
# Process finished with exit code 0

# if

var_flag = True

if var_flag == True:
    print('Astazi este miercuri!')
else:
    print('Astazi este o zi de weekend!')

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\base.py
# Astazi este miercuri!
# Process finished with exit code 0

# sirul meu de numere de la 0 la 19
for i in range(20):
    if i % 2 == 0:
        # impartire la 2 cu rest
        print('Numarul {} este par: ', i)

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\base.py
# Astazi este miercuri!
# Numarul {} este par:  0
# Numarul {} este par:  2
# Numarul {} este par:  4
# Numarul {} este par:  6
# Numarul {} este par:  8
# Numarul {} este par:  10
# Numarul {} este par:  12
# Numarul {} este par:  14
# Numarul {} este par:  16
# Numarul {} este par:  18
#
# Process finished with exit code 0

# sirul meu de numere de la 0 la 19
for i in range(20):
    if i % 2 == 0:
        # impartire la 2 cu rest
        print('Numarul {} este par: ', i)
    # print(i)
    else:
        print('Numarul {} este impar: ', i)

# sirul meu de numere de la 0 la 19
for i in range(20):
    if i % 2 == 1:
        # impartire la 2 cu rest
        print('Numarul {} este impar: ', i)

# C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\base.py
# Astazi este miercuri!
# Numarul {} este impar:  1
# Numarul {} este impar:  3
# Numarul {} este impar:  5
# Numarul {} este impar:  7
# Numarul {} este impar:  9
# Numarul {} este impar:  11
# Numarul {} este impar:  13
# Numarul {} este impar:  15
# Numarul {} este impar:  17
# Numarul {} este impar:  19
#
# Process finished with exit code 0


# sirul meu de numere de la 0 la 19
for i in range(20):
    if i % 2 == 0:
        # impartire la 2 cu rest
        print(f'Numarul {i} este par')