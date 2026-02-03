text = """

Strings can be manipulated in many ways!
You can split them, slice them, and change their case. 

    Indentation matters sometimes. 
Whitespace can be tricky. 

Have fun exploring string methods like: 
lower(), upper(), strip(), replace(), and split()

"""

print("Functie care numara cuvintele dintr-un string:")

def count_words(string1):
    return (len(string1.split(" ")))

result = count_words(text)
print(result)

print("Exemplu simplu de explicat logica:")

string3 = "Hello happy world"
print (len(string3.split(" ")))

print("Functie care numara toate cuvintele care incep cu i sau I:")

def count_words_starting_i(string1):
    words_list = string1.split()
    total = 0
    for word in words_list:
        if word.startswith("i") or word.startswith("I"):
            total = total + 1
    return total

result2 = count_words_starting_i(text)
print(result2)

print("Genereaza un raport:")

def generate_report(string1):
    word_count = count_words(string1)
    words_starting_i = count_words_starting_i(string1)

    report = f"""
Din sirul de caractere original, avem in total: 
{word_count} Cuvinte
{words_starting_i} Cuvinte care incep cu i 
"""
    return report

report = generate_report(text)
print(report)


print("Converting to class:")

#text_processor1 = TextProcessor(text)
#report2 = text_processor1.generate_report()
#print(report2)

class TextProcessor:
    # constructor
    def __init__(self, param1):
        self.text = param1

    #metoda1
    def count_words(self):
        return (len(self.text.split(" ")))

    # metoda2
    def count_words_starting_i(self):
        words_list = self.text.split()
        total = 0
        for word in words_list:
            if word.startswith("i") or word.startswith("I"):
                total = total + 1
        return total

    # metoda3
    def generate_report(self):
        #word_count = count_words(string1)
        word_count = self.count_words()
        #words_starting_i = count_words_starting_i(string1)
        words_starting_i = self.count_words_starting_i()
        report = f"""
Din sirul de caractere original, avem in total: 
{word_count} Cuvinte
{words_starting_i} Cuvinte care incep cu i 
"""
        return report

text_proc1 = TextProcessor(text)
print(text_proc1.count_words())
print(text_proc1.count_words_starting_i())
print(text_proc1.generate_report())

# explicare sau clarificare parametri pentru functii

print("=====================Parametri============================")
print()

# variabila trebuie sa fie definita inainte de functie, altfel da eroare

print("Printare param1:")

param1 = "Hello" # param1 e numele unei variabile
print(param1)

print("Printare din functie varianta 1:")

def fc1(p1):
    print(p1)
    print(param1)

fc1("This is not a hello")

print("Printare din functie varianta 2:")

# se defineste o functie
def fc1(param1):
    print(param1)

# se apeleaza acea functie
fc1("This is not a hello")

print("Printare din functie varianta 3:")
# se defineste o functie
def fc1(param1):
    print(param1)

def fc2():
    return "Another Hello!"

# se apeleaza acea functie
fc1("This is not a hello")
fc1(fc2())
fc1(param1)

print("Printare din functie varianta 4:")

def fc3(param2, param3, param1):
    print(param2)
    print(param3)
    print(param1)

fc3("2", "3", "1")

print("Printare din functie varianta 5:")

def fc3(param2=10, param3=20, param1=30):
    print(param2)
    print(param3)
    print(param1)

fc3()

print("Printare din functie varianta 6:")

def fc3(p1, param2=10, param3=20, param1=30):
    print(p1)
    print(param2)
    print(param3)
    print(param1)

fc3("Not hello")

print("Printare din functie varianta 7:")

def fc3(p1, param2=10, param3=20, param1=30):
    print(p1)
    print(param2)
    print(param3)
    print(param1)

fc3("Not hello", 100)

print("Printare din functie varianta 8:")

def fc3(p1, param2=10, param3=20, param1=30):
    print(p1)
    print(param2)
    print(param3)
    print(param1)

fc3("Not hello", param1 = 100)

print("Printare din functie varianta 9:")

def fc3(p1, param2=10, param3=20, param1=30):
    print(p1)
    print(param2)
    print(param3)
    print(param1)

fc3("Not hello", param2=4, param3=99, param1=50)


#C:\playground\PyBase\.venv\Scripts\python.exe C:\playground\PyBase\08_classes.py
#Functie care numara cuvintele dintr-un string:
#39
#Exemplu simplu de explicat logica:
#3
#Functie care numara toate cuvintele care incep cu i sau I:
#2
#Genereaza un raport:
#
#Din sirul de caractere original, avem in total:
#39 Cuvinte
#2 Cuvinte care incep cu i
#
#Converting to class:
#39
#2
#
#Din sirul de caractere original, avem in total:
#39 Cuvinte
#2 Cuvinte care incep cu i
#
#=====================Parametri============================
#
#Printare param1:
#Hello
#Printare din functie varianta 1:
#This is not a hello
#Hello
#Printare din functie varianta 2:
#This is not a hello
#Printare din functie varianta 3:
#This is not a hello
#Another Hello!
#Hello
#Printare din functie varianta 4:
#2
#3
#1
#Printare din functie varianta 5:
#10
#20
#30
#Printare din functie varianta 6:
#Not hello
#10
#20
#30
#Printare din functie varianta 7:
#Not hello
#100
#20
#30
#Printare din functie varianta 8:
#Not hello
#10
#20
#100
#Printare din functie varianta 9:
#Not hello
#4
#99
#50
#
#Process finished with exit code 0