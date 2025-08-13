global_var = True
var1 = 10

# Local Scopes : Variables defined inside a function
def local_scope():
    x=10
    print(x)
    
# global scopes
def fetchGlobalVar():
    print(global_var)
    
fetchGlobalVar()

# Changing a global variable : incorrect
def change_global_incorrect():
    var1 = 20
    print(var1)

change_global_incorrect()    
print(var1)

# Changing a global variable : correct
def change_global_correct():
    global var1
    var1 = 20
    
change_global_correct()
print(var1)

# Accessing variable between scopes: For nested functions
def outer_func():
    print("Outer function")
    outer_var = 10
    def inner_func():
        print("Inner function")
        print(outer_var)
    
    inner_func()
        
outer_func()

# Modifying variables between scopes: For nested functions
def outer_func2():
    outer_var2 = 10
    def inner_func2():
        nonlocal outer_var2
        outer_var2 = 20
    inner_func2()
    print(outer_var2)
    
outer_func2()
