
# 1. Sum of elements
numbers = [6,5,3,8,4,2,5,4,11]

sum = 0
for i in numbers:
    sum = sum+i
print(f'Sum of numbers in List is: {sum}')

# using range() method
sumofnumbers = 0
for j in range(17,15285,17):
    sumofnumbers = sumofnumbers+j
print(f'Sum of numbers in range is: {sumofnumbers}')

print("*"*30)

# Nested For Loop
adj = ['red','big','tasty']
fruits = ['apple','banana','cherry']

for i in adj:
    for j in fruits:
        print(i,j)

print("*"*30)

# Using For Loop with else
for i in range(10):
    print(i)
else:
    print("List finished")

print("*"*30)

# Using zip() method to print lists together
adj1 = ['red','big','tasty']
fruit = ['apple','banana','cherry']

for x,y in zip(fruit,adj1):
    print(x,y)

print("*"*30)


# Accessing Dictionary elements by For Loop
dic = {'name':'Azhar','age':20}
for key,value in dic.items():
    print(key,value)
