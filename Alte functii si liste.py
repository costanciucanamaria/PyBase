# DIN RECORDING
from operators_strings import my_string

print("=======================Lower====================================")

test_name = "VoltageCheck"

print(test_name.lower())

print("=======================Comanda====================================")


command = "StaRt"

# vreau sa folosesc aceasta comanda pentru a porni un sistem oarecare


if command == "start":
    print("Starting system") # -> aici nu afiseaza nimic

if command.lower() == "start":
    print("Starting system") # -> chiar dcaa utilizatorul scrie gresit o comanda, scade riscul de eroare

print("=======================string_indexing====================================")

# cum pot accesa dintr-un string un anumit caracter

word = "Python"

# vreau sa afisez prima litera

print("=========prima_litera===========")

print(word[0])

print("=========a_treia_litera===========")

print(word[3])

print("=========ultima_litera===========")

print(word[-1])


print("=========mai_multe_caractere===========")


text = "Programming"

print("=========# vreau sa afisez primele 6 caractere===========")


print(text[0:6])

print("=========# vreau sa imi afisez de la inceput pana la un anum caracter===========")

print(text[:4])

print("=========#varianta_inversa===========")

print(text[4:])

# aceste operatii sunt utile cand lucram cu siruri de caractere


print("=========# vreau sa cunosc lungimea unui string===========")

message = "Hello Python"

print(len(message))

print("=========# concatenare===========")

a = ("Hello")
b = ("World")

print("=========fara spaatiu===========")

print (a + b) #-> apare legar

print("=========cu spatiu===========")

print (a + " " + b) # -> apare cu spatiu

print("=========curatare spatii===========")

raw = "     ERROR_CODE_12  "

print(raw)

clean_string = raw.strip()
print(clean_string)

print("=========replace===========")

log = "Voltage=12,5V"

# vreau sa inlocuiesc virgula cu punct

print(log)

# cu virgula valoarea mea nu e recunoscuta ca si float, de aceea trb sa modific virgula cu punct
# altfel as abea probleme cu codul mai tarziu

log = log.replace(",",".")
print(log)

log1 = "Voltage=12,5V new text1, text2"
log1 = log1.replace(",",".")
print(log1)

print("=========vreau doar anumite fisiere luate in considerare===========")

file_name = "report_2025.log"

if file_name.endswith(".log"):
    print("Log file detected")

file_name1 = "xreport_2025.exe" #-> aici nu afiseaza nimic

if file_name1.endswith(".log"):
    print("Log file detected")

if file_name.startswith("report"):
    print("Report file detected")

if file_name1.startswith("report"): #-> aici nu afiseaza nimic
    print("Report file detected")

print("=========find===========")

message = "CAN timeout detected"

# vreau sa vad daca in mesajul meu se gaseste cuvantul cheie timeout

imdex = message.find("timeout") #-> 4
print(imdex)

imdex1 = message.find("exit") #-> -1 -> nu l-am gasit
print(imdex1)

print("=========in vs find===========")

Timeout_flag = False

if "timeout" in message:
    Timeout_flag = True
    print("timeout found!")

# daca imi parasesc if-ul, nu ma mai pot lega de rezultatul lui in restul codului, doar daca pun un flag

print("=========split===========")
print("===========================")
print("===========================")


# aceasta metoda face split la un text in mai multe stringuri

data = "12.5,3.7,OK"

# vreau sa faca split in 3 noi stringuri, virgula sa fie delimitarea

print("=========initial===========")

print(data)

print("=========split===========")

values = data.split(",")
print(values) #-> imi genereaza o lista

print("=========join===========")


my_strings = ["Ana ", "are ", "mere", "!"]
final_string = "".join(my_strings)
print(final_string)

print("=========path===========")


# am parti dintr-un path dintr-un fisier
# as vrea sa creez path-ul final pentru a fi folosit in cod

parts = ["C:", "logs", "2026", "run_01.txt"]

path = "/".join(parts)
print(path)

# am ramas la 01:02:04

