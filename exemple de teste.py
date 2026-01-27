v1 = "Hello World"
#     1234567891011 (si spatiul e un caracter)
#     -11-10-9-8-7-6-5-4-3-2-1
# la -12 da eroare
print(v1[0], v1[1], v1[-1])



# tip de data primitiva:
print("daca lasam codul de mai jos, se printeaza 10")

x1 = 10

def change(x1):
    x1 = 11
    return x1

change(x1) # fii atent aici

print(x1)

print("daca lasam codul de mai jos, se printeaza 11")

x1 = 10

def change(x1):
    x1 = 11
    return x1

x1 = change(x1)

print(x1)

# tip de data complex:

print("daca folosim o lista se printeaza [11]")


x2 = [10]

def change(x1):
    x2[0] = 11

change(x2)

print(x2)

#C:\playground\PyBase\.venv\Scripts\python.exe "C:\playground\PyBase\exemple de teste.py"
#H e d
#daca lasam codul de mai jos, se printeaza 10
#10
#daca lasam codul de mai jos, se printeaza 11
#11
#daca folosim o lista se printeaza [11]
#[11]
#
#Process finished with exit code 0