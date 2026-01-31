student = {
    "name": "Adrian",
    "age": 32,
    "weight": 70.0,
    "backpack": ["keys", "wallet", "camera", "phone"],
    0: "nothing at all",
    (1,2): "alpha and omega" # se accepta si tupluri
}

student2 = {
    "name": "Marius",
    "age": 25,
    "weight": 65.0,
    "backpack": []
}

student3 = {
    "name": "Catalin",
    "age": 30,
    "weight": 80.0,
    "backpack": ["keys", "wallet", "camera"],
    0: "nothing at all",
    (1,2): "alpha and omega" # se accepta si tupluri
}

# Acesti studenti au anumite proprietati la comun
# Putem crea o functie care extrage ce este in ghiozdanul fiecaruia

print("Returnati ce au studentii in ghiozdan:")

# functia aceasta trebuie sa extraga ghiozdanul de la oricare student de mai sus si lucreaza cu un parametru (variabila din interior), nu direct cu variable din exterior
def get_backpack(param1):
    return param1["backpack"]

print(get_backpack(student3))

# print(get_backpack(100)) # TypeError: 'int' object is not subscriptable -> numarul 100 nu este in dictionar si nu apare nici in backpack

print("=====================================Clase==================================================")
print("Cea mai simpla clasa")

class Dog:
    pass     # inseamna nimic deocamdata

# o clasa e un fel de fabrica pt obiecte ale acelei clase
# e ca o idee abstracta a unor entitati sau lucruri din lumea programarii
# dog este o clasa
# cand scriu numele clasei cu paranteze creez o instanta a clasei care este o variabila
print("Print var1:")

var1 = Dog()
print(var1)
# asa apare: <__main__.Dog object at 0x000002753DCE4C20> -> main e primul fisier unde se incepe rularea programului; Dog e clasa acestui fisier; var1 e un obiect de tipul Dog
# si e stocat undeva in memoria RAM
print("Print var1:")
print(var1)
# daca printez de 2 ori, primesc exact acelasi text: <__main__.Dog object at 0x000001DD12D74C20>
# var1 este si o instanta si un obiect, in engleze sunt interschimbabile
# pana si dictionarul este un obiect
# instanta si clasa sunt diferite
print("Print var2:")
var2 = Dog()
print(var2) # <__main__.Dog object at 0x0000024D05EB8E10> -are alte numere
print("Print var3:")
var3 = Dog()
print(var3) # <__main__.Dog object at 0x0000012513CE8F50>
print("Print var4:")

var4 = Dog()

var4.name = "Spot" # proprietate a clasei
var4.owner = "Iulian"
var4.legs = 4
var4.last_vaccine = 2025
print("Printare proprietatea name:")

print(var4.name)
print("Printare proprietatea owner:")

print(var4.owner)
print("Printare proprietatea legs:")

print(var4.legs)
print("Printare proprietatea last_vaccine:")

print(var4.last_vaccine)
print("Printare toate proprietatile:")

print(var4.__dict__)

var5 = Dog()
var5.name = "Shadow"
print("Printare toate proprietatile:")

print(var5.__dict__)
print("Printare clasa la mai multe variable:")

print(var5.__class__)
print(var4.__class__)

# cum arata un constructor pt o clasa:
# un constructor e o functie sau o metoda care prim niste prametri si atribuie oniectului creat acele proprietati
class Cat:
    # constructor:
    def __init__(self, name, owner, legs, last_vaccine=None):    # self e o referinta la instanta/obiectul din acest moment la care lucram
        self.name = name
        self.owner = owner
        self.legs = legs
        self.last_vaccine = last_vaccine
    # metoda:
    def make_sound(self):
        print(self.name, "Meowww!")
    # alta metoda:
    def take_a_bite(self, param1):
        a_bite = param1.pop(0)
        print(f"{self.name} took a bite of {a_bite}.")

# def __init__(self, param1, param2, param3, param4=None):
#     self.name = param1
#     self.owner = param2
#     self.legs = param3
#     self.last_vaccine = param4

# python umple automat acest self
# last_vaccine=None inseamna ca e optional (default parameter)

var6 = Cat("Missy", "Vlad", 4, 2025)
print(var6)
print(var6.__dict__)

var7 = Cat("KitKat", "Ana-Maria", 4) # pisica nu a fost vaccinata
print("Printare toate proprietatile:")

print(var7.__dict__)
print("Printare owner:")

print(var7.owner)

var7.make_sound()
var6.make_sound()

print(var6.name)
print(var7.name)
print(var7.owner)


#def take_a_bite(self, param1):
#    a_bite = param1.pop()  -> La pop scoate ultimul din lista
#    print(f"{self.name} took a bite of {a_bite}")

snacks = ["fish_snack", "meat_popsickle", "milk", "fresh_rat", "catnip"] # e in afara clasei
var7.take_a_bite(snacks)
var7.take_a_bite(snacks)
var7.take_a_bite(snacks)
var7.take_a_bite(snacks)
var7.take_a_bite(snacks)
