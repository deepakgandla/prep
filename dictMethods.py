#ways to create dictionary
student = {'name' : 'Deepak', 'rollNo' : 68}
student = dict(name='Deepak', rollNo=68)
student = dict([('name', 'Deepak'), ('rollNo', 68)])
print(student)

#fromkeys : Returns a dictionary with the specified keys and value
keys = [1,2,3]
value = 0
d = dict.fromkeys(keys, value)
print(d) #output {1: 0, 2: 0, 3: 0}

#get : Returns the value of the specified key
print(student.get('name'))

#items : Returns a list containing a tuple for each key value pair
print(student.items()) #output dict_items([('name', 'Deepak'), ('rollNo', 68)])

#keys : Returns a list containing the dictionary's keys
print(student.keys()) #output dict_keys(['name', 'rollNo'])

#values : Returns a list of all the values in the dictionary
print(student.values()) #output dict_values(['Deepak', 68])

#update : Updates the dictionary with the specified key-value pairs
student.update({"Grade" : "A"})
print(student)

#pop : Removes the element with the specified key
print(student.pop('Grade')) #ouput A
print(student) #output {'name': 'Deepak', 'rollNo': 68}

#popitem : Removes the last inserted key-value pair
student['age'] = 21
print(student) #output {'name': 'Deepak', 'rollNo': 68, 'age': 21}
student.popitem()
print(student) #output {'name': 'Deepak', 'rollNo': 68}

#setdefault : Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
x = student.setdefault('name', 'John')
print(x) #output Deepak
y = student.setdefault('weight', 75)
print(y) #output 75
print(student) #output {'name': 'Deepak', 'rollNo': 68, 'weight': 75}
