# Simple Calculator By Using Python
operator = input()       # Enter the operator
Number_1 = int(input())  # Enter The Number 1
Number_2 = int(input())  # Enter The Number 2

if operator == " + ":              #Addition 
    Addition = Number_1 + Number_2
    print(Addition)
elif operator == " - ":            #Difference
    Difference = Number_1 - Number_2
    print(Difference)
elif operator == " * ":            #Multification
    Multification = Number_1 * Number_2 
    print(Multification)
elif operator == " / ":            #Division
    Division = Number_1 / Number_2
    print(Division)
elif operator == " % ":            #Module
    Module = Number_1 % Number_2
    print(Module)

