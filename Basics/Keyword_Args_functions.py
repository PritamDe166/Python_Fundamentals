def kwargs_func(**students):
    for key, value in students.items():
        print(f"{key} : {value}")
        
kwargs_func(name="Pritam", age=30, city= "Bangalore")


def pet_details1(**details):
    if "name" in details:
        print(f"name : {details['name']}")
    else:
        print("Hello pet")
        

pet_details1(name = "Tommy", species ="Dog")


# Example 3: With other positional arguments

def pet_details2(pet_type, **pet_details):
    for key, value in pet_details.items():
        return f"Welcome your pet {pet_type}, {key} is {value}"

print(pet_details2("Dog", name = "Tommy", age = 3))