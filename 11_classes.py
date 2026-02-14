print("==================Mostenire pentru clase======================")

# Cand mostenesti o clasa, acea clasa e parintele celeilalte clase
# ne putem folosi de modelele si functiile originale, ori le putem suprascrie

print("Exemplu foarte simplu:")

class Animal:
    def __init__(self, name="Amoeba"):
        self.name = name

    def action(self):
        print("I'm searching for food!")


class Cat(Animal):
    def __init__(self, stripes, name = "Cat"):  #daca stripes era dupa name, avea nevoie de default
    #non-default parameter needs to be on the left side, and all paramaters with default value need to be on the right
        super().__init__(name)
        self.stripes = stripes

    def purr(self):
        print("I purr!")

    def putem_defini_o_metoda_foarte_explicita(self):
        print("I jump!")

    def action(self):         #semnatura unei metode (daca scriem  def action(self, param1, param2) e alta semnatura
        super().action() # acest super() acceseaza clasa parinte
        print("Hunting for mice and rats!")  #acest action il inlocuieste pe cel din clasa animal

class Dog(Animal):
    def action(self):
        print("Runs around, looking for squirrels!")
        print("Licks your face afterwards!")

print("animal:")

anim1 = Animal("Lizard")
anim1.action()  #aici apare: I'm searching for food!
print(anim1.name)

print ("===========================================================")
print("pisica:")

cat1 = Cat("Red", "Leo")
cat1.purr()                # Pisica a mostenit metoda de la animal si are si metoda ei proprie (purr)
cat1.action()
cat1.putem_defini_o_metoda_foarte_explicita()
print(cat1.name)
print(cat1.stripes)

print ("===========================================================")

print("caine:")
dog1 = Dog()
dog1.action()

print ("===========================================================")\

print("Animal Park:")

cat2 = Cat( "Orange", "Skitty")
cat3 = Cat( "Black", "Skittles")
dog2 = Dog("Hunter")
dog3 = Dog("PawPaw")

animal_park = [cat2, cat3, dog2, dog3]

for v in animal_park:
    print(v.name)
    v.action()

#C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\11_classes.py
#==================Mostenire pentru clase======================
#Exemplu foarte simplu:
#animal:
#I'm searching for food!
#Lizard
#===========================================================
#pisica:
#I purr!
#I'm searching for food!
#Hunting for mice and rats!
#I jump!
#Leo
#Red
#===========================================================
#caine:
#Runs around, looking for squirrels!
#Licks your face afterwards!
#===========================================================
#Animal Park:
#Skitty
#I'm searching for food!
#Hunting for mice and rats!
#Skittles
#I'm searching for food!
#Hunting for mice and rats!
#Hunter
#Runs around, looking for squirrels!
#Licks your face afterwards!
#PawPaw
#Runs around, looking for squirrels!
#Licks your face afterwards!
#
#Process finished with exit code 0