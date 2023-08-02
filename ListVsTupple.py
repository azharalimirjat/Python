"""
LIST:
    A Python list is an ordered and changeable collection of data objects.
==> List is mutable.
TUPLE:
    A Python list is an ordered and unchangeable collection of data objects.
==> Tuple is immutable list.

Differences b/w List and Tuple

1. => List is mutable
   => Tuple is immutable

2. => List elements are written in []
   => Tuple elements are  in ()
"""

# Mutable list: It means we can change elements in existing list
list=[12,23,34,45,65,2,4,1,44,55,66]
print("List Before change: ")
print(list)
list[3]=3434
print("List after change: ")
print(list) # 45 replaced with 3434


# Immutable List:
tuple = (12,34,65,64,76,87,4,6,23,8,79,88)
print("Tuple elements before change")
print(tuple)
# tuple[0]=23 # wrong
print(tuple) # You will get an error because this is tuple and it is immutable


"""
Packing Tuple:
    When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

Unpacking Tuple:
    we are  allowed to extract the values back into variables. This is called "unpacking":
"""
# Packing Table:
fruits = ("apple", "banana", "cherry")


# Unpacking Tuple:
fruits = ("apple", "banana", "cherry")
print(fruits)

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
