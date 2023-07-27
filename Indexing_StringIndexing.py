"""
Indexing:
    It means accessing an element by its position

==> Indexing starts from 0 (From left to right).
==> Indexing starts form -1(From right to left)

STRING INDEXING:
    Strings are ordered sequences of character data,
    and the individual characters of a string can be accessed
    directly using that numerical index.
"""

# Ex:
name = "Azhar Ali Mirjat"
# Accesing M (Its index number is 10)
print(name[10]) #Output will be " M "

# We can access any character by its index number
# Index means its position number


# Ex: Indexing from Right to left
nam = "Shahid Ali"
print(nam[-3]) #Output will be " A "


#Left to Right Indexing
print("Printing Shahid Ali by indexing from Left to Right")
print(nam[0]) #output " S "
print(nam[1]) #output " h "
print(nam[2]) #output " a "
print(nam[3]) #output " h "
print(nam[4]) #output " i "
print(nam[5]) #output " d "
print(nam[6]) #output "  "
print(nam[7]) #output " A "
print(nam[8]) #output " l "
print(nam[9]) #output " i "

print("Printing Shahid Ali by indexing from Right to Left")
print(nam[-1])  #output " i "
print(nam[-2])  #output " l "
print(nam[-3])  #output " A "
print(nam[-4])  #output "  "
print(nam[-5])  #output " d "
print(nam[-6])  #output " i "
print(nam[-7])  #output " h "
print(nam[-8])  #output " a "
print(nam[-9])  #output " h "
print(nam[-10]) #output " S "


print("Printing Shahid Ali by indexing from Left to Right descending")
print(nam[-10]) #output " S "
print(nam[-9])  #output " h "
print(nam[-8])  #output " a "
print(nam[-7])  #output " h "
print(nam[-6])  #output " i "
print(nam[-5])  #output " d "
print(nam[-4])  #output "  "
print(nam[-3])  #output " A "
print(nam[-2])  #output " l "
print(nam[-1])  #output " i "


# Showing characters by giving a range
"""
firstname = Azhar Ali
print from A to r
we will write : print(firstname[startingpoint:endingpoint])
"""
firstname = "Azhar Ali"
print(firstname[0:5]) #output " Azhar " It will exclude last given position means (5-1)


# Excluding a character
"""
lastname= "Azhar Ali"
we will write print(lastname[startingposition:endingposition+1:positiontobeskipped])
EX: print(lastname[0:5:2])
here 2 is position to be skiped
"""

lastname= "Azhar Ali"
print(lastname[0:5:2]) #Output Azar

print(lastname[0::]) #means start from zero and go till end
# Output " Azhar Ali "


print(lastname[0::2]) #Means leaves every 2nd position character
# Output " AhrAi "
