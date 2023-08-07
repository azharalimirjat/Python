"""
DICTIONARY:
    Dictionaries are used to store data values in key:value pairs.
==> A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

SYNTAX:
    variable_name = {'key':'value'}
"""

# Example:
dictionary = {'key':"value"}
print(dictionary)
# OUTPUT: {'key':"value"}

# We can also write multiple key & value pairs in one dictionary
dict_a = {'key1':'Azhar', 'key2':'Mirjat', 'key3':22323}

"""
===> We can write above dict_a as:
dict_a = {'key1':'Azhar', 
          'key2':'Mirjat',
          'key3':22323
          }
"""

print(dict_a)
# OUTPUT: {'key1':'Azhar', 'key2':'Mirjat', 'key3':22323}



"""
RETRIEVING VALUES FROM DICTIONARY:
    It means accessing value from existing dictionary.
Synatx:
1. print(dictionary_name[key])

Examples:
"""

cities_dictionary = {'key1':'Jamshoro', 'key2':'Larkana', 'key3':'Karachi', 'key4':'Sukkur', 'key5':'Multan'}

# Accesing whole dictionary
print(cities_dictionary)


# Accesing only one city, we use key to access that city
print(cities_dictionary['key2'])
# OUTPUT: Larkana


# ==> If key does not exist in dictionay you will get an error in output
# We use get() method here to avoid error
print(cities_dictionary.get('key6'))
# If key does not exist,you will get 'None' as output
