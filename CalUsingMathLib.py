#Calculator in python using functions and math libaray
import math

print("\t Calculator \t")


print("1- add \n")
print("2- subtract \n")
print("3- multiply \n")
print("4- division \n")
print("5- Exponent of 1st to 2nd \n")
print("6- sine of 1st num \n")
print("7- Print cos of 1st \n")
print("8- Print tan of 1st \n")
print("9- Find ceil of 1st \n")
print("10- Find floor of second \n")
print("11- Find percentage of first wrt second \n")


def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


def multiply(x, y):
    return x*y


def divide(x, y):
    return x/y


def exp(x, y):
    return x**y


def sin(x):
    return math.sin(x)


def cos(x):
    return math.cos(x)


def tan(x):
    return math.tan(x)


def ceil(x):
    return math.ceil(x)


def floor(x):
    return math.floor(x)


def percentage(x, y):
    result = (x/y)*100
    return result


while True:
    choice = int(input("Enter your choice : "))

    if 1 <= choice <= 11:
        num1 = float(input("Enter 1st number : "))
        num2 = float(input("Enter 2nd number : "))

        if choice == 1:
            print(num1 , "+", num2, " = ", add(num1, num2))

        elif choice == 2:
            print(num1 , "-", num2, " = ", subtract(num1, num2))

        elif choice == 3:
            print(num1, "*", num2, " = ", multiply(num1, num2))

        elif choice == 4:
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == 5:
            print(num1, "^", num2, " = ", exp(num1, num2))

        elif choice == 6:
            print("Sine of ", num1, " is: ", sin(num1))

        elif choice == 7:
            print("Cosine of ", num1, " is: ", cos(num1))

        elif choice == 8:
            print("Tangent of ", num1, " is: ", tan(num1))

        elif choice == 9:
            print("Ceil of ", num1, " is : ", ceil(num1))

        elif choice == 10:
            print("Floor of ", num2, " is : ", floor(num2))

        elif choice == 11:
            print("Percentage of ", num1, "wrt ", num2, " is ", percentage(num1,num2), "%")