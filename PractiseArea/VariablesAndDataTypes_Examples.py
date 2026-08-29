#Create variables for your name, age, height, and whether you are employed — print all of them with their types using type()
name = "Pritam"
age = 35
height = 5.8
employed = False

print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")
print(f"Height: {height}, Type: {type(height)}")
print(f"Employed: {employed}, Type: {type(employed)}")



print("City: {city}, Country: {country}, Pin_code: {pin_code}".format(city = "Bangalore", country = "India", pin_code = 12345))


city , country, pin_code = "Bangalore", "India", 12345
print(f"City: {city}, Country: {country}, Pin_code: {pin_code}")