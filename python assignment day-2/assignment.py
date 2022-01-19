print("\t\t\t DATA TYPES AND PRINT STATEMENTS !")
name = "shyam"
age = 20
total_marks = 75.76
complex_number = 1+5j
items_in_list = ["pen", 'pencil', 10, 5.5, True]
items_in_tuple = ("tomato", 'onion', 65, 50, False)
items_in_set = {"dog", 'cat', "rabbit"}
items_in_dictionary = {
    "door.no": 10,
    "street": "Gandhi street",
    "city": "Chennai",
    "state": "Tamil Nadu",
    "nation": "India"
}
print("\t\t\t FIRST FORMAT IN PRINT STATEMENT")
print(" My name is " + name + " and age is " + str(age) + ".\n" + " I have scored " + str(total_marks) +
      ".\n" + " The items in my list is " + str(items_in_list) + ".\n" + " The items in my tuple is "
      + str(items_in_tuple) + ".\n" + " The items in my set " + str(items_in_set) + ".\n" +
      " The items in my dictionary is " + str(items_in_dictionary))
print("\n")
print("\t\t\t SECOND FORMAT IN PRINT STATEMENT")
print(" My name is %s and age is %d. I have scored %f" % (name, age, total_marks))
print(" The items in my list is %s" % items_in_list)
print(" The items in my tuple is %s" % (items_in_tuple,))
print(" The items in my set is %s" % items_in_set)
print(" The items in my dictionary is %s" % items_in_dictionary)
print("\n")
print("\t\t\t THIRD FORMAT IN PRINT STATEMENT")
print(""" My name is {} and age is {}.\n I have scored {}.\n The items in my list is {}.
 The items in my tuple is {} .\n The items in my set {}.
 The items in my dictionary is {}"""
      .format(name, age, total_marks, items_in_list, items_in_tuple, items_in_set, items_in_dictionary))
print("\n")
print("\t\t\t FOURTH FORMAT IN PRINT STATEMENT")
print(f" My name is {name} and age is {age}. I have scored {total_marks}")
print(f" The items in my list is {items_in_list}")
print(f" The items in my tuple is {items_in_tuple}")
print(f" The items in my set is {items_in_set}")
print(f" The items in my dictionary is {items_in_dictionary}")
