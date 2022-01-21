print("\t\t\t FUNCTIONS 1: ALL DATA TYPES ")
def data_types(name, roll_number, subject_and_code, marks, total_marks, result, percentage):
    print(f" Name: {str(name)} \n Roll Number: {int(roll_number)} .\n"
          f" The subject and their code: {dict(subject_and_code)} \n"
          f" Marks in individual subjects: {set(marks)} .\n Result in the subjects: {list(result)}.\n"
          f" Total marks obtained in all semester: {tuple(total_marks)} .\n"
          f" Total percentage in all semester: {float(percentage)}")


data_types("shyam", 123456, {
    "CODES": "SUBJECT",
    "COA01": "English",
    "COA02": "Tamil",
    "COA03": "Maths",
}, {75, 80, 83}, ["pass", "pass", "pass"], (238, 250, 225, 260, 275, 255), 79.34)
print("\n\n")
print("\t\t\t FUNCTION 2: DICTIONARY USING FOR LOOP")
def for_loop():
    address = {
        "car": "Lamborghini",
        "phone": "Apple",
        "bike": "Royal Enfield"
    }
    for i, j in address.items():
        print(f" My favourite is {i} and favourite brand is {j}")


for_loop()
print("\n\n")
print("\t\t\t FUNCTION 3: PRINT TWO NUMBERS IN LIST")
def numbers(a, b):
    return [a, b]


c = numbers(10, 20)
print(f" The Two Numbers are in list: {c}")
print(type(c))
