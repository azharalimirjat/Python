"""
LOGICAL OPERATORS:
    Python has three Boolean operators, or logical operators: and , or , and not .
    You can use them to check if certain conditions are met before deciding the
    execution path your programs will follow.
 Operators are:
 1. AND
 2. OR

 Examples:
"""

# AND: Returns true if all conditions are true.
a=1
b=3

print(b!=a and b>=a) #Output: True => b/c both conditions are true


# OR: Returns true if any of the given conditions is true
print(b!=a or b<=a) #Output: True => b/c one condition is true


a=3
b=6

c= (a>b or b!=a) and (a<b or b>a)
print(c) # Output: True
# NOTE: We can write multiple conditions using logical operators.
