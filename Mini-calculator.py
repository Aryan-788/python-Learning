# Mini calculator using python
print("*** MINI CALCULATOR ***")

num1 = float(input("Enter 1st Number:- "))
num2 = float(input("Enter 2nd Number:- "))

print("Press 1 for Addition: ")
print("Press 2 for Subtraction: ")
print("Press 3 for Multiplication: ")
print("Press 4 for Division: ")

choice = int(input("Choose the number that you have to calculate :- "))

if choice == 1:
    print("The Addition of given two number is ", num1 + num2)

elif choice == 2:
    print("The Subtraction of given two number is ", num1 - num2) 

elif choice == 3: 
    print("The Multiplication of given two number is ", num1 * num2)

elif choice == 4:
    print("The Division of given two number is ", num1 / num2)

else:
    print("Invalid Input")
 
