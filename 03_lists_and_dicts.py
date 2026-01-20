lista1 = ["apple", "orange", "banana"]
lista2 = [30, 50, 100]
lista3 = [3, 10, 4, 100, 35, 50, 90, 87, 99, 500, 1000, 1]
# index   0   1  2   3   4   5   6   7  8    9     10   11

print(lista3)

# lista3[1:3] -> [10, 4]
# slice syntax: list_variable[start_slice:end_slice] -> start si end sunt indecsi
# prin indecsi manipulam lista, vedem elementele din lista

print(lista3[1:3]) # -> [10, 4]
print(lista3[1:4]) # -> [10, 4, 100]

# faceti un slice de la mijlocul listei pana la sfarsit

print(lista3[4:9]) # -> [35, 50, 90, 87, 99]

print(lista3[4:11])

# cum rezolvam dinamic?
# care este mijlocul listei? care e sfasitul listei?


# n+1/2 -> Cum aflam n? n fiind nr de elemente din lista

# // operartor de impartire intreaga 3 //2 -> 1 ; 3/2 -> 1.5


print(lista3[(len(lista3) + 1 )// 2:len(lista3)])


#C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\03_lists_and_dicts.py 
#[3, 10, 4, 100, 35, 50, 90, 87, 99, 500, 1000, 1]
#[10, 4]
#[10, 4, 100]
#[35, 50, 90, 87, 99]
#[35, 50, 90, 87, 99, 500, 1000]
#[90, 87, 99, 500, 1000, 1]
#
#Process finished with exit code 0


lista1 = ["apple", "orange", "banana"]
#           0       1           2
#           -3     -2          -1
lista2 = [30, 50, 100]


print(lista1[-3])

print(lista1 + lista2)
print(lista2 + lista1)

# daca vreau ca in lista 1 sa adaug elementele din lista 2?

lista4 = lista1 + lista2

lista1.extend(lista2)

print(lista1)
print(lista4)



#C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\03_lists_and_dicts.py 
#apple
#['apple', 'orange', 'banana', 30, 50, 100]
#[30, 50, 100, 'apple', 'orange', 'banana']
#['apple', 'orange', 'banana', 30, 50, 100]
#['apple', 'orange', 'banana', 30, 50, 100]
#
#Process finished with exit code 0

lista1.remove("banana")
print(lista1)

#C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\03_lists_and_dicts.py 
#['apple', 'orange', 30, 50, 100]
#
#Process finished with exit code 0



print("============sortare=============================")

lista5 = [3, 10, 4, 100, 35, 50, 90, 87, 99, 500, 1000, 1]
lista5.sort()
print(lista5)
lista5.sort(reverse=True)
print(lista5)

lista5.reverse()
print(lista5)

#C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\03_lists_and_dicts.py 
#============sortare=============================
#[1, 3, 4, 10, 35, 50, 87, 90, 99, 100, 500, 1000]
#[1000, 500, 100, 99, 90, 87, 50, 35, 10, 4, 3, 1]
#[1, 3, 4, 10, 35, 50, 87, 90, 99, 100, 500, 1000]
#
#Process finished with exit code 0