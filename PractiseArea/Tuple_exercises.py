# create a tuple
coordinates = (10.3, 13.5, 14.1)
print(coordinates)

single_el_tuple = (10.4,) #single element tuple. Without the comma, it's just an integer
print(single_el_tuple)

# Accessing elements. Same as list
print(coordinates[1])
print(coordinates[-1]) # Last element

# Slicing. Same as list
print(coordinates[0:2])

# Common methods (limited because immutable)
print(len(coordinates))
print(coordinates.count(10.3)) #count occurances
print(coordinates.index(14.1))
print(coordinates.index(14.1))

# Looping
for pt in coordinates:
    print(pt)

# Unpacking tuples. Very Imp
x, y, z = coordinates
print(x, y, z, sep = " ,")