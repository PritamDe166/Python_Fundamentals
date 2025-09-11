# Types of collections data types in Python:

# 1. List
employee_ages = [23,21,23,34,45, 61, 34, 19, 45, 67, 89, 90, 12, 34, 56, 78, 90, 12, 34, 56, 78, 90]
# employee_ages.sort()          # Sort the list in ascending order
# employee_ages.append(100)     # Add a new age to the list
# employee_ages.remove(12)        # Remove the age we just added
print("Employee Ages:", employee_ages)



# 2. Tuple
coordinates = (10.3, 13.5, 14.1)
print("The location is:", coordinates)
# Tuples are immutable, meaning they cannot be changed after creation

# 3. Set
''' 
Realtime scenario, where we have a  list of ip addresses that visits a site, we want to know the count of unique ip addresses, so in this scenario we will use set
to get the unique ip addresses fromthe list
'''

visitors = [
    "192.168.1.1",
    "10.0.0.5",
    "192.168.1.1",  # Duplicated
    "172.16.0.3",
    "10.0.0.5"      # Duplicated
]

unique_visitors = set(visitors)  # Convert the list to a set to get unique IP addresses

print("Unique Visitors:", len(unique_visitors))

# Math Operations using Set
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a & b)  # Intersection of two sets
print(a | b) # Union of two sets without duplicates


# 4. Dictionary
# Syntax 
employee_details = {
    "name" : "Pritam",
    "age" : 30,
    "department" : "IT",
    "height" : 5.9
}

print("Employee Details:", employee_details)

# Real life sceanrio for Dictionary
'''
You are building a student information system. Each student has a unique ID, and you want to store and retrieve their details (like name, age, and grade) efficiently.
Use a dictionary where the key is the student ID and the value is another dictionary holding their details.'''

student_Details = {
    "S101" : { "name" : "Pritam" , "age" : 20, "grade" : "A"},
    "S102" : { "name" : "Rahul" , "age" : 22, "grade" : "B"},
    "S103" : { "name" : "Priya" , "age" : 21, "grade" : "A"}
}

# update values
student_Details["S101"]["grade"] = "A+"
print("Updated Details for S101 : ", student_Details["S101"])

# Add new student
student_Details["S104"] = { "name" : "Anita" , "age" : 23, "grade" : "B+"}

print("All Student Details:", student_Details)