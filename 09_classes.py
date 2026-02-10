#class Dog:
#    def __init__(self, name, owner):
#        self.name = name
#        self.owner = owner
#
#
#dogvar1 = Dog("Spot", "Iulian")
#print(dogvar1)

#C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\09_classes.py
#<__main__.Dog object at 0x00000298A1124D70>
#
#Process finished with exit code 0



class Cat:
    def __init__(self, name, owner = None):
        self.name = name
        self.owner = owner

    # ac. metoda trb. sa returneze un string gol; converteste Cat in string
    def __str__(self):
        if self.owner is None:
            return f"Cat: {self.name}"
        else:
            return f"Cat: {self.name}, with owner: {self.owner}"

    def __repr__(self):
        return f"Cat('{self.name}', '{self.owner}')"


catvar1 = Cat("Spot", "Iulian")
print(catvar1)
catvar2 = Cat("Shadow")
print (catvar2)

# facem o lista de pisici

pisici = [catvar1, catvar2]
print(pisici) # [<__main__.Cat object at 0x000001AB33DE4EC0>, <__main__.Cat object at 0x000001AB33DD8E10>]
              # fara metoda def __repr__(self):

cats = [Cat('Spot', 'Iulian'), Cat('Shadow', 'None')] #am luat cu copy paste din rezultatul listei pisici (datorita def __repr__(self):)
print (cats)

#reprezentare_str = str(catvar1)  # -> converteste in string
#print(reprezentare_str)          #[<__main__.Cat object at 0x0000028A0B624D70>, <__main__.Cat object at 0x0000028A0B618E10>]
#print(type(reprezentare_str))  # <class 'str'>
#print (type(catvar1))            # <class '__main__.Cat'>


catvar3 = Cat("Ginger", "Oscar")
catvar4 = [catvar3] # astfel se poate copia codul

print(catvar3)  # Cat: Ginger, with owner: Oscar
print(catvar4)  # [Cat('Ginger', 'Oscar')]