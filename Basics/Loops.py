# Exercises in FOR loop

# Exercise 1: Print numbers from 1 to 10
for i in range(1, 11):
    print(i)
    
# Exercise: Print each character ina string
name = "Pritam"
for c in name:
    print(c)
    
#Exercise: Sum of numbers in a list
list_of_numbers = [5, 4, 7, 8, 9, 10, 54]
current_sum = 0
for i in list_of_numbers:
    current_sum = current_sum + i

print("sum is: ", current_sum)


#Exercise: Multiplication table of 5
multiply_limit = int(input("Enter the limit for multiplication table: "))

for i in range(1, multiply_limit + 1):
    print(5*i)
    
    
# Exercises for WHILE loop

# Exercise: Countdown from 5 to 1
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
    
# Exercise: Keep asking the user to enter the password until they get it right
user_password = ""
correct_password = "System@123"

while user_password != correct_password:
    user_password = input("Enter a password: ")
    
    
# Exercise : Sum of the first N Numbers
numbers_limit = int(input("Enter the upper range of numbers to add: "))
current_sum = 0
while numbers_limit > 0:
    current_sum = current_sum + numbers_limit
    numbers_limit -= 1
print("The sum is: ", current_sum)