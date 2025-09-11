#Print()
print("-------print()-------")
print("This is a normal print") # Basic Print
print("Python","is","fun")      # Multiple values
print("apple","mango","banana", sep=", ")  # Using Separators
print(1,2,3, end=" ")
print(4,5,6)

#input()
print("--------input()-------")
name = input("Enter Name: ")
print(name)


# format() - format strings
print("Welcome {}, you are {} years old".format("Pritam", 34))

print("Welcome {0}, you are {1} years old".format("Payal", 33)) # Positional arguments
print("Welcome {name}, you are {age} years old".format(name="Pritam",age=34)) # Keyword Arguments


# f-strings 
name="Pritam"
age=34
print(f"Hello {name}, you are {age} years old")
