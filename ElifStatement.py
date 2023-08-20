"""
Elif Statement
     elif is short for "else if" and is used when the first if statement isn't true,
    but you want to check for another condition.

Syntax:
if (condition1):
    print("if If statement is true")
elif (condition2):
        print("if If statement is false")
elif (condition3):
        print("if upper statements are false")
elif (conditionN): #Nth means, there can be multiples conditions.
        print("if Upper statements are false")
else:
    print("if all conditions are false")
"""

# Example with two conditions
sound = input('what sound you like: ')

if sound == 'meow':
    print("You Love Cats.  Cat Person")
elif sound == 'wuff':
    print("You Love Dogs")
else:
    print("You do not love cats")



# Example with multiple conditions
# Checking grade in a subject according to given marks

marks = int(input('Enter your marks: '))

if marks>=91:
    print("You got A+ Grade")
elif marks>=83 & marks<=90:
    print("You got A Grade")
elif marks>=75 & marks<=82:
    print("You got B+ Grade")
elif marks>=65 & marks<=74:
    print("You got B Grade")
elif marks>=60 & marks<=64:
    print("You got C+ Grade")
elif marks>=50 & marks<=59:
    print("You got C Grade")
else:
    print("You Failed the Subject")
