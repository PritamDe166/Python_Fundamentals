from operator import indexOf
import math

fruits = ["apple", "orange", "banana", "strawberry", "kiwi", "peach", "mango", "lichi"]

print(fruits[1])
print(fruits)
print(fruits[-1]) # index from the end

print(fruits[1:5]) # prints everything from index 1 to 4...5 is not included

fruits.append("grapes") # insert at the end
print(fruits)

fruits.insert(2,"papaya")
print(fruits)

fruits.pop() #remove last item
print(fruits)

fruits.pop(2) # remove by index
print(fruits)

fruits.remove("peach") # remove by value
print(fruits)


#looping through a list
for item in fruits:
    if item == "orange":
        print(indexOf(fruits,"orange")) # prints the index of "orange" in the item


# sorting
nums = [6, 4, 9, 8, 10, 15, 3, 7]
nums.sort()         # sorts in place
print(sorted(nums)) # returns new sorted nums



###############################################

#Create a list of 5 of your favourite movies

movies_list = ["Titanic", "Inception","Avatar","Shawshank Redemption"]
print(movies_list[0], movies_list[-1], sep = ", ") # Print the first and last movie

movies_list.append("Blade Runner") # Add a new movie at the end
print(movies_list)

movies_list.pop(1)
print(movies_list)

print(f"Total Count is movies : {len(movies_list)}")

nums2 = [10, 20, 30, 40, 50]
print(nums2[1:4])


