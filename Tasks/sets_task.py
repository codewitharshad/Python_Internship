# Task 1 – Create a set of 5 fruits
fruits = {"Apple", "Banana", "Mango", "Orange", "Grapes"}
print(fruits)


# Task 2 – Add 2 new fruits using add() and update()
fruits.add("Pineapple")
fruits.update(["Papaya"])
print(fruits)


# Task 3 – Remove one fruit using discard()
fruits.discard("Banana")
print(fruits)


# Task 4 – Create two sets of numbers and find set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)


# Task 5 – Check if an element exists in a set
if "Apple" in fruits:
    print("Apple exists in the set")
else:
    print("Apple does not exist in the set")


# Task 6 – Create a frozen set and try to add an element
frozen_numbers = frozenset([1, 2, 3])
print(frozen_numbers)

frozen_numbers.add(4)