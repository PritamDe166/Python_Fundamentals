# Exercise 1
def exercise1():
    var1 = "Pritam"
    print(var1)

exercise1()

# Exercise 2 : Accessing global variable
var2 = "This is 1st global variable"

def exercise2():
    print(var2)
    
exercise2()
print(var2)


# Exercise 3: Modify global variable
var3 = "This is 2nd global variable"

def exercise3():
    global var3
    var3 = "This is 2nd global variable modified"
    print(var3)
    
exercise3()
print(var3)

# Exercise 4: Modify global variable counter
counter1 = 0

def increase_counter():
    global counter1
    counter1 += 1

increase_counter()
print(counter1)

# Exercise 5: Enclosing scope with nested functions

def outerfunction1():
    message = "This variable is in inner function"
    
    def innerfunction1():
        print(message)
        
    innerfunction1()
    print(message)
    
outerfunction1()

# Exercise 6: Enclosing scope: Modifying variables within nested functions

def outerfunction2():
    message = "This variable is in the outer function"
    
    def innerfunction2():
        nonlocal message
        message = "This variable has been modified in the inner function"
    innerfunction2()
    return message

print(outerfunction2())