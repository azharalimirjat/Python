# 1. Concatenation
list1 = [1, 2, 3, 'a', 'b', 'c']
list2 = [4, 5, 6, 'd', 'e', 'f']

# Method_01: by using + sign
list3 = list1 + list2
print(list3)

# Method_02: by extending
list1.extend(list2)
print(list1)

# Addind element in the existing the list,

# Method_01: by append() method
list1.append("h")
print(list1)

# Method_02: by extend method
list1.extend("g")
print(list1)

# remove(): Removing any element from the existing list.
print("Removing any Element from the existng list")
listremove = [3, 4, 5, 6, 7]
print(listremove)
listremove.remove(4)
print(listremove)

# by pop() method, this will remove last element of the list
list1.pop()

# count(): Counting given element to know repeatation
citylist = ["Jamshoro", "Karachi", "Larkana", "Hyderabad", "Dadu", "Larkana"]
print(citylist.count("Larkana"))

# Sort(): Sorting given element in list, If elements are in string data type then it sorts alphabetically
# If elements are numbers than sorts number as whole numbers.
citylist = ["Jamshoro", "Karachi", "Larkana", "Hyderabad", "Dadu", "Larkana"]
citylist.sort()
print(citylist)

# reverse(): This method reverse the order of the given element
listofnumbers = [1, 25, 7, 5, 65, 45, 343, 233]
print(listofnumbers)
listofnumbers.reverse()
print(listofnumbers)  # reversed list


# There are so many other methods try, you may try by yourself.
