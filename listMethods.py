fruits = ['apple', 'banana', 'cherry']

#append : adds an element to the end of the list
fruits.append('mango')
print(fruits)

#count : returns the number of times specified element occured
print(fruits.count('apple'))

#extend : add elements of a list or an other iterbale, to the end of the current list
fruits.extend(['orange', 'papaya'])
print(fruits)

#reverse : Reverses the order of the list
fruits.reverse()
print(fruits)

#sort : Sorts the lis
fruits.sort()
print(fruits)

#index : returns the index of the first element with the specified value
print(fruits.index('orange'))

#insert : adds element at specified postion
fruits.insert(1, 'grape')
print(fruits)

#pop : removes the element at the specified position
fruits.pop(5)
print(fruits)

#remove : removes the first item with the specified value
fruits.remove('grape')
print(fruits)

#copy : Returns a copy of the list
newls = fruits.copy()
print(newls)

#clear : removes all the elements from the list
fruits.clear()
print(fruits)
