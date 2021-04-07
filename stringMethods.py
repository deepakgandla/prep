name='deepak'

#Converting first charcater to upper case using capitalize string method
newName=name.capitalize()
print(name, newName) #output: deepak Deepak

#counting number of times a specified value occured in newName
print(newName.count('e')) #output 2

#endswith returns true if string ends with specified value else returns false
print(newName.endswith('ak')) #output true

#startswith retuns true if string starts with specified value else reutns false
print(newName.startswith('D')) #output true
print(newName.startswith('d')) #output false
print(newName.startswith('De')) #output true

#index method returns the index of the specified value
print(newName.index('pa')) #output 3

#lower method converts string into lower case
print(newName.lower()) #output deepak
print(newName) #output Deepak

#upper method coverts string into upper case
print(newName.upper()) #output DEEPAK

#Split method is used to split the the string at the specified separator, and returns a list
sentence='Good Morning all'
ls=sentence.split(' ')
print(ls) #output ['Good', 'Morning', 'all']

#join method Joins the elements of an iterable to the end of the string
newSentence='*'.join(ls)
print(newSentence) #output Good*Morning*all

#strip mehthod is used to return trimmerd version of a string
badStr='     hey       '
updatedStr=badStr.strip()
print(updatedStr) #output hey

#title method is used to convert the first character of each word to upper case
movie='once upon a time in hollywood'
title=movie.title()
print(title) #output Once Upon A Time In Hollywood

print(newName.index('e')) #output 1
print(newName.rindex('e')) #output 2
print(newName.find(('e'))) #output 1
print(newName.rfind('e')) #output 2