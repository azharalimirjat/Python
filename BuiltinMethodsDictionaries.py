
# Using Built-in methods in Dictionaries.

# list in Dictionary and dictionary inside dictionary
car_dic = { 'model':'Corola',
            'year':[2012,2015,2018,2021],
            'docs':{'original':'yes', 'dupicate':'no'}
          }

# Changing value(Corola) using it's key(model)
car_dic['model'] = 'Toyota'
print(car_dic)
# Model changeg from Corola to Toyota


# Adding new key:value pair
car_dic['tyres'] = 'yes' #Added this key:value pair to car_dic
print(car_dic)


# items() method will show each key:value pair separately
print(car_dic.items())

# We can also access any key:value pair separate by giving them names
# EX:
a,b,c,d = car_dic.items()
print(a)
print(d) #Output: ('tyres', 'yes')
print(c)
print(d)


# We can also access only keys names using keys() method.
# EX:
key1,key2,key3,key4 = car_dic.keys()
print(car_dic.keys()) #Output: All keys in singles row

# Unpacked keys
print(key1) #Output: model
print(key2) #Output: year
print(key3) #Output: docs
print(key4) #Output: tyres



# We can also access only values names using values() method.
# EX:
value1,value2,value3,value4 = car_dic.values()
print(car_dic.values()) #Output: All values in single row

# Unpacked values
print(value1) #Output: Toyota
print(value2) #Output: [2012, 2015, 2018, 2021]
print(value3) #Output: {'original': 'yes', 'dupicate': 'no'}
print(value4) #Output: yes


# We can remove last key:value pair using key by pop() mehtod
car_dic.popitem()
print(car_dic) #tyres key with its value has be removed from dictionary



# We can remove any key:value pair using key by pop() mehtod
car_dic.pop('model')
print(car_dic) #model key with its value has be removed from dictionary
