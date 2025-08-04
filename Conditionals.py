num = 7
if num%2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
    
    
# Exercise: Take input from user and check if the number is even or odd

num = int(input("Enter a number: "))

if num < 0:
    print("The number is negative.")
elif num == 0:
    print("The number is zero.")
elif num%2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
    

# Exercise: Compare two numbers and print the larger one, or if they are equal.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 >num2:
    print("The 1st number is greater than the second number")
elif num1 < num2:
    print("The 2nd number is greater than the first number")
else:
    print("The numbers are equal")
    
    
# Exercise : Take a score between 0–100 and print the grade:

num = (int(input("Enter your score: ")))

if num < 60:
    print("You have Failed")
elif num >= 60 and num < 70:
    print("Your Grade is: D")
elif num >= 70 and num < 80:
    print("Ypur Grade is : C")
elif  num >= 80 and num < 90:
    print("Your Grade is: B")
else:
    print("Your Grade is: A")