# Program to enter full name and store first and last name separately
full_name = input("Enter your full name: ")
splitted = full_name.split()
print(splitted)

length = len(splitted)

first_name = splitted[0]
last_name = splitted[-1]
print("First Name: {}".format(first_name))
print("Last Name: {}".format(last_name))
if length > 2:
    middle_name = splitted[1:-1]
    print("Middle Name: ", end="")
    for each in middle_name:
        print(each, end=" ")