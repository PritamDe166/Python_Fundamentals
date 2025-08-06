# Positional Arguments
def postional_example(name:str, age:int, city:str):
    return f"Welcome {name}!! You are from {city} and you are {age} years old."

print(postional_example("Pritam", 33, "Bangalore"))


# Default parameters
def default_example(name:str, age:int, city = "Chennai"):
    return f"Welcome {name}!! You are from {city} and you are {age} years old."

print(default_example("Pritam", 33))
print(default_example("Payal", 32, "Bangalore"))


# Multiple Default parameters

def default_ex_mult(name:str, age = 30, city = "bangalore"):
    return f"Welcome {name}!! You are from {city} and you are {age} years old."

print(default_ex_mult("Pritam"))


# *args Variable Positional Arguments

def variable_args(*numbers):
    for num in numbers:
        print(num)
        
variable_args(12, 1, 10, 15, 19, 20)


# Example 1: With Regular parameters

def var_args(greeting, *names):
    for name in names:
        print(f"{greeting}! {name}") 
    
var_args("Welcome", "Pritam", "Payal", "Ram")


# Same example where the function returns something instead of printing

def var_args(greetings, *names):
    greet = []
    for name in names:
        greet.append(f"{greetings}! {name}")
    return greet
        
result = var_args("Welcome", "Pritam", "Payal", "Rahul")
for item in result:
    print(item)
    

# Exercise: find squares of inputs

def square_calc(*nums):
    return [num**2 for num in nums]

result = square_calc(2, 6, 9, 10, 12)
for number in result:
    print(number)