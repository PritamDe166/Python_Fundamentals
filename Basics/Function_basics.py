from typing import Union

def grades(num):
    if num > 80:
        return "Grade A"
    elif num < 80 and num > 60:
        return "Grade B"
    else:
        return "Grade C"
    
    
number_to_compare = int(input("Enter number to compare: "))
print(grades(number_to_compare))


# Exercise: With multiple return values

def calculator_func(a: int, b:int) -> int:
    return a+b, a-b, a*b, a/b


added, subtracted, multiplied, divided = calculator_func(4, 2)

print("addtion result: ", added)
print("substraction result: ", subtracted)
print("multiplication result: ", multiplied)
print("division result: ", divided)


# Exercise: With named parameters and return types

def greetings(age:int, name:str) -> str:
    return f"Hello! {name} . Your age is {age}"

print(greetings(26, "pritam"))


# Exercise: Functions returning none

def greet_print(name:str, age:int) -> None:
    print(f"Hello {name}, your age is {age}")
    
    
greet_print("Pritam", 32)


# Exercise: With list and tuple

def average_func(list_numbers: list[float]) -> float:
    return sum(list_numbers)/len(list_numbers)

print(average_func([3.4, 4.5, 6.2, 5.3]))


# Exercise: Returning multiple types

def parse_age(age:int) -> Union[str, None]:
    if age > 0:
        return f"Hello! Your age is {age}"
    else:
        return None
    
print(parse_age(21))