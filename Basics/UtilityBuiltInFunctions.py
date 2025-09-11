# help()
help(len)
help(list)

#dir(obj)
print(dir("string"))
print(dir([]))

#id(obj)
list1 = ["apple", "mango", "banana"]
print(id(list1))
list2 = list1
print(id(list2))

# any(iterable)
list3 = [0, True, ""]
print(any(list3))

list4 = [0, "", False]
print(any(list4))

# all(iterable)
list5 = [1, True, "pritam"]
print(all(list5))

list6 = [1, True, ""]
print(all(list6))

#zip(iterables)
list6 = ["apple", "mango", "banana"]
list7 = [9, 6, 3, 1]

zipped = zip(list6, list7)
print(list(zipped))