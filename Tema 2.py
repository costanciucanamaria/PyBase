print("1. Creati o lista de numere de la 1 la 100, din 3 in 3, folosind range(), exemplu de lista: [0, 3, 6, 9, 12, 15,......]")
from statistics import median

lista = list(range(0, 100, 3))

print("Aici este lista de numere:", lista)

print("======================================================================================================================================================================")

print("2. Adaugati la sfarsitul listei numere de la 300 la 600, din 10 in 10, sa arate lista in urmatorul fel: [0, 3, 6, ....., 99, 300, 310, 320, ....., 590, 600]")

lista.extend(range(300, 601, 10))

print("Aici sunt numerele adaugate:", lista)

print("======================================================================================================================================================================")

print("3. Stergeti din lista mare numerele 51, 54, 66, 400.")

nr_de_sters = [51, 54, 66, 400]

for numar in nr_de_sters:
    if numar in lista:
        lista.remove(numar)

print("Aici este lista cu numerele sterse:", lista)

print("======================================================================================================================================================================")

print("4. Numarati cate numere se afla in lista.")

print("Numar de elemente:", len(lista))

print("======================================================================================================================================================================")

print("5. Calculati suma tuturor numerelor din lista. Calculati media acestui total.")

suma = sum(lista)
media = suma/len(lista)

print("Suma:", suma)
print("Media:", media)

print("======================================================================================================================================================================")

print("6. Inversati lista, sa fie sortata de la cel mai mare numar la cel mai mic numar.")

lista.sort(reverse=True)

print("Aici este lista inversata de la mare la mic:", lista)

print("======================================================================================================================================================================")

print("7. Printati cel mai mare numar din lista.")

print("Cel mai mare numar din lista:", max(lista))

print("======================================================================================================================================================================")

print("8. Faceti un slice din lista, de la mijloc pana la sfarsitul listei.")

lista.sort(reverse=False)

de_la_mijloc_incolo = len(lista) // 2
print("Slice de la mijloc spre sfarsit:", lista[de_la_mijloc_incolo:])

#C:\playground\PyBase\.venv\Scripts\python.exe "C:\playground\PyBase\Tema 2.py"
#1. Creati o lista de numere de la 1 la 100, din 3 in 3, folosind range(), exemplu de lista: [0, 3, 6, 9, 12, 15,......]
#Aici este lista de numere: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
#======================================================================================================================================================================
#2. Adaugati la sfarsitul listei numere de la 300 la 600, din 10 in 10, sa arate lista in urmatorul fel: [0, 3, 6, ....., 99, 300, 310, 320, ....., 590, 600]
#Aici sunt numerele adaugate: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600]
#======================================================================================================================================================================
#3. Stergeti din lista mare numerele 51, 54, 66, 400.
#Aici este lista cu numerele sterse: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 57, 60, 63, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600]
#======================================================================================================================================================================
#4. Numarati cate numere se afla in lista.
#Numar de elemente: 61
#======================================================================================================================================================================
#5. Calculati suma tuturor numerelor din lista. Calculati media acestui total.
#Suma: 15062
#Media: 246.91803278688525
#======================================================================================================================================================================
#6. Inversati lista, sa fie sortata de la cel mai mare numar la cel mai mic numar.
#Aici este lista inversata de la mare la mic: [600, 590, 580, 570, 560, 550, 540, 530, 520, 510, 500, 490, 480, 470, 460, 450, 440, 430, 420, 410, 390, 380, 370, 360, 350, 340, 330, 320, 310, 300, 99, 96, 93, 90, 87, 84, 81, 78, 75, 72, 69, 63, 60, 57, 48, 45, 42, 39, 36, 33, 30, 27, 24, 21, 18, 15, 12, 9, 6, 3, 0]
#======================================================================================================================================================================
#7. Printati cel mai mare numar din lista.
#Cel mai mare numar din lista: 600
#======================================================================================================================================================================
#8. Faceti un slice din lista, de la mijloc pana la sfarsitul listei.
#Slice de la mijloc spre sfarsit: [99, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600]
#
#Process finished with exit code 0