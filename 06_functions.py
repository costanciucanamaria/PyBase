print("====================Curs Functii 6==========================")

print("Punem in practica tot ce am invatat")
print("=============================================")
print("Exercitiu 1")
print("=============================================")
print("Primim o lista de numere intregi. Separati-le in numere pare si impare si salvati rez intr-un dictionar")
print("Returnati dictionarul cu rezultat.")

#ex_dictionar = {
#    "odd_numbers": [3, 5, 11, 13, 201],
#    "even_numbers": [2, 4, 8, 10, 12, 200, 340],
#    "odd_total" = 233,
#    "even_total": 444
#}


def is_even(nr):
    return nr % 2 == 0

def list_total(list1):
    total = 0
    for n in list1:
        total = total + n
    return total

def process_data(list1):
    result = {}
    odd_list = []
    even_list = []

    for n in list1:
        if is_even(n):
            even_list.append(n)
        else:
            odd_list.append(n)


    result["odd_numbers"] = odd_list
    result["even_numbers"] = even_list
    result["odd_total"] = list_total(odd_list)
    result["even_total"] = list_total(even_list)
    return result

    print(odd_list)
    print(even_list)

data_list = [0, 5, 11, 31, 40, 52, 100, 999]

var2 = process_data(data_list)

print(var2)

print("==============================================================================================================")

print("In Py mai avem niste unelte built in pe care le putem folosi:")
print("map(), filter(), reduce(), sorted(), functii lambda")
print("==============================================================================================================")
print("Map:")

lista2 = [3, 5, 10, 20]

# eu pot sa apelez o functie map peste o alta lista de numere; daca apelez map(lista2) se ia intreaga lista si se face o operatie, innultita cu 2
# 3    -> 6
# 5    -> 10
# 10   -> 20
# 20   -> 40

def mult_2(nr):
    return nr * 2

result1 = list(map(mult_2, lista2))
print (result1)

def pow_2(nr):
    return nr ** 2

result2 = list(map(pow_2, lista2))
print (result2)

#lista3 = []
#
#for x in lista2:
#    lista3.append(x*2)
#
#for x in lista2:
#    lista3.append(mult_2(x))
#
#print (lista3)
#
#
print("Lambda:")
# O functie lambda are proprietati specifice ei. Una dintre ele e ca ea, functia in sine, este anonima.

#def div_5(x):
#    return x/5   # asta e la fel cu lambda

result2 = list(map(lambda x: x/5, lista2)) # mai incolo nu pot sa apelez lambda, exista doar in ac moment, in acest punct

print (result2)

result3 = list(map(lambda x: x//5, lista2))
print (result3)

print("Lambda_functie_neanonima:")

functie_neanonima = lambda a,b: a+b
print(functie_neanonima(3,6))

print("Filter:")

print("Filter True - Toate trec")

nr_pare = list(filter(lambda x: True, lista2))
print(nr_pare)

print("Filter False - Nimic nu trece")

nr_pare = list(filter(lambda x: False, lista2))
print(nr_pare)

print("Filter Numere pare")

nr_pare = list(filter(lambda x: x % 2 == 0, lista2))
print(nr_pare)

print("Filter Numere impare")

nr_pare = list(filter(lambda x: x % 2 != 0, lista2))
print(nr_pare)

print("Mai facem un map")

lista5 = [7, 10, 14, 13, 30, 60]

#Exemplu:
#rezult = {
#    7: "impar",
#    10: "par",
#    14: "par",
#    13: "impar",
#    30: "par",
#    60: "par"
#}

strings = list(map(lambda x: "par" if x%2 == 0 else "impar", lista5))

print(strings)

result = {}
for i in range(len(lista5)):
    nr = lista5[i]
    choice_nr = strings[i]
    result[nr] = choice_nr

print(result)

#lambda x: "par" if x%2 == 0 else "impar"
#Echivalent:

#def par_impar(x):
#    if x % 2 == 0:
#        return "par"
#    else:
#        return "impar"


print("==============================================================================================================")

print("Reduce:")

#C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\06_functions.py
#====================Curs Functii 6==========================
#Punem in practica tot ce am invatat
#=============================================
#Exercitiu 1
#=============================================
#Primim o lista de numere intregi. Separati-le in numere pare si impare si salvati rez intr-un dictionar
#Returnati dictionarul cu rezultat.
#{'odd_numbers': [5, 11, 31, 999], 'even_numbers': [0, 40, 52, 100], 'odd_total': 1046, 'even_total': 192}
#==============================================================================================================
#In Py mai avem niste unelte built in pe care le putem folosi:
#map(), filter(), reduce(), sorted(), functii lambda
#==============================================================================================================
#Map:
#[6, 10, 20, 40]
#[9, 25, 100, 400]
#Lambda:
#[0.6, 1.0, 2.0, 4.0]
#[0, 1, 2, 4]
#Lambda_functie_neanonima:
#9
#Filter:
#Filter True - Toate trec
#[3, 5, 10, 20]
#Filter False - Nimic nu trece
#[]
#Filter Numere pare
#[10, 20]
#Filter Numere impare
#[3, 5]
#Mai facem un map
#['impar', 'par', 'par', 'impar', 'par', 'par']
#{7: 'impar', 10: 'par', 14: 'par', 13: 'impar', 30: 'par', 60: 'par'}
#==============================================================================================================
#Reduce:
#
#Process finished with exit code 0