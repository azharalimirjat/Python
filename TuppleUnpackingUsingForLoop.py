
Tuple = [(1,2),(3,4),(5,6)]

# Accessing only two values from list
# a,b = Tuple => You will get an error
# You have to access all elements of tuple at a time manually


# Accessing values from tuple using For Loop

for a,b in Tuple:
    print(a,b)

# Example:02
# Make list of tuple with range() funtion
x = tuple(list(range(10)))
for i in x:
    print(i)


# Enumerate() Function
# It gives element values with their indexes

fruits = ('Apple','Banana','Orange','Pineapple')
for index, value in enumerate(fruits):
    print(index,value)
