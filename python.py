print("Calculator ")
print("Functions in Calculator are ")
print("SUM , SUBTRACT , DIVIDE , MULTIPLY ,POWER ")


num1 = float(input("Enter 1st number : "))
num2 = float(input("Enter 2nd number : "))
result = str(num1+num2)

print("Addition of above two : " + result)
result = str(num1*num2)

print("Multiplication of above two is : " + result )
result = str(num1-num2)

print("Subtraction of above two is : " + result)

result = str(num1/num2)
print("Division of above two numbers is : " + result)

result = str(num1**num2)
print("Result of  " + str(num1) + "^^" + str(num2) + " is : " + result)

print("Percentage of a number  ")
per = float(input("Enter a number whose %age to be find : "))
total = float(input("Enter the total amount for which you want to find percentage : \n"))
result = str((per/total)* 100)
print("Percentage of " + str(per) + "wrt" + str(total) + 'is :' + result + "%")












