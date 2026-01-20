raw_logs = [
"   ERROR | Voltage too LOW | code=E12",
"   info | System started successfully",
"   WARNING | High temperature detected | code=W07",
"   ERROR | Communication timeout | code=E99",
"   info | System shutdown complete"
]

for i in range(len(raw_logs)):
    # for i -> creaza o variabila i
    # len(raw_logs) -> 5
    # range(len(raw_logs)) -> range (5) -> [0, 1, 2, 3, 4]

    # raw_logs -> lista
    # raw_logs[i] -> un element din lista -> string
    # lista nu contine strip()
    # string contine strip()


    # 1.Clean each log line
    # For every log entry:Remove leading and trailing spaces and convert it to lowercase
    # Must use: strip(), lower()

    raw_logs[i] = raw_logs[i].strip().lower()

    #2.split log fields
    #now instead of raw_logs being a list of strings, it's a list of lists of strings
    #Must use: split("|")

    raw_logs[i] = raw_logs[i].split("|")

    print(raw_logs[i])


    #3. identify log level
    # detect whether the log is: error, warning, info
    # must use: in, startswith()
    # trebuie sa trecem prin fiecare lista si sa ne uitam la primul element din lista

print("--------------Starting Identification------------------")

log_type_counts = []

#inainte de for initializam listele (pt punctul 5)

error_codes_list = []
warning_codes_list = []


#print(log_type_counts)

for i in range(len(raw_logs)):
    # raw_logs[i] -> ['error', 'voltage too low', 'code=e12']
    # raw_logs [i][0] -> 'error'
    # raw_logs [i][0][0] -> prima litera din error -> 'e'
    # print(raw_logs[i][0])
    # is_error = raw_logs[i][0].startswith("error")
    if raw_logs[i][0].startswith("error"):
        # log_type_counts.append("error")
        log_type_counts.append(raw_logs[i][0].strip())
        print("Ce eroare avem?")
        print(raw_logs[i][2])


        # 5. Extract error / warning codes
        # From lines that contain "code=", extract the code value.
        # Example: "code=e12" → "E12"
        # Must use: split("="), upper()
        # procesam eroarea din logul cu erori:
        # raw_logs[i][2].split("=") -> ne va returna o lista cu 2 elemente ['code', 'E12']
        # raw_logs[i][2].split("=")[1]
        extracted_error_code = raw_logs[i][2].split("=")[1]
        error_codes_list.append(extracted_error_code)

    if raw_logs[i][0].startswith("info"):
        # log_type_counts.append("info")
        log_type_counts.append(raw_logs[i][0].strip())

    if raw_logs[i][0].startswith("warning"):
        # log_type_counts.append("warning")
        log_type_counts.append(raw_logs[i][0].strip())
        print("Ce warning avem?")
        print(raw_logs[i][2])

        extracted_error_code = raw_logs[i][2].split("=")[1]
        warning_codes_list.append(extracted_error_code)


# 4. count log types
# count how many errors, warnings, info messages we have
# must use count()
# ca sa numaram, trebuie sa le gasim cu if-ul de mai sus
# trebuie sa le bagam in lista

# am numarat cate sunt error, cate sunt warning, cate sunt info

error_count = log_type_counts.count("error")
warning_count = log_type_counts.count("warning")
info_count = log_type_counts.count("info")



# Aceasta este solutia preliminara:

#print("OUTPUT")
#print("LOG SUMMARY")
#print("-------------")
#print("Errors  : ")
#print(log_type_counts.count("error"))
#print("Warnings: ")
#print(log_type_counts.count("warning"))
#print("Info    : ")
#print(log_type_counts.count("info"))

# multiline:
# un f string iti permite sa formatezi anumite parti ale string-ului; se pune f in fata stringului

output_string = f"""
OUTPUT
LOG SUMMARY
-------------
Errors  : {error_count}
Warnings: {warning_count}
Info    : {info_count}

Error Codes: {error_codes_list}
Warning Codes: {warning_codes_list}
"""

print(output_string)
print(error_codes_list)
print(warning_codes_list)



