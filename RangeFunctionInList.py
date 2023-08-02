"""
RANGE() FUNCTION IN LIST:
    The range() function returns a sequence of numbers, starting from 0 by default,
    and increments by 1 (by default), and stops before a specified number.

SYNTAX:
range(start, stop, step)

start	Optional. An integer number specifying at which position to start. Default is 0
stop	Required. An integer number specifying at which position to stop (not included).
step	Optional. An integer number specifying the incrementation. Default is 1

Examples below:
"""

# 10 Whole Numbers list from 0 to 9
wholeNumberList = list(range(10))
print(wholeNumberList)


# Even Numbers List
evenList = list(range(2,100,2))
print(evenList)


# Odd Numbers List
oddNumbers = list(range(1,100,2))
print(oddNumbers)
