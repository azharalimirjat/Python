"""
Iterator and Iterable:
     Iterators power and control the iteration process,
     while iterables typically hold data that you want
     to iterate over one value at a time.

"""

list = [1,2,3,4,5,6,7,8,9]

# iter(value): this method is used to make any value iterable
var_a = iter(list)
print(var_a)
# For above Output:  <list_iterator object at 0x0000019C063E9630> (address)
# It shows that the list has been iterable

# For printing value we use next(value) method
print(next(var_a)) # Output: 1(first value of list)


# Method#01: used next(value) method as many times as you want the value to be printed or used

print(next(var_a)) # Output: 2
print(next(var_a)) # Output: 3
print(next(var_a)) # Output: 4
print(next(var_a)) # Output: 5
print(next(var_a)) # Output: 6
print(next(var_a)) # Output: 7
print(next(var_a)) # Output: 8
print(next(var_a)) # Output: 9

# you can use this on Dictionary, sets and Strings as well

# Method#02: Use For Loop
# This is an easy way to access all values in one go.
print('For Loop is being used here')
for var_b in list:
    print(var_b)
