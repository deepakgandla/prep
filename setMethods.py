nums1 = {1,2,2,2,3,4,5}

#add : Adds an element to the set
nums1.add(6)
print(nums1) #output {1, 2, 3, 4, 5, 6}

#update : adds the specified values to the current set
nums1.update({10,11,12})
print(nums1)  #output {1, 2, 3, 4, 5, 6, 10, 11, 12}

#remove : removes specified element from the list
nums1.remove(11)
print(nums1) #output {1, 2, 3, 4, 5, 6, 10, 12}

#difference : Returns a set one containing the difference between two or more sets
nums2={5,6,7,8}
print(nums1.difference(nums2)) #output {1, 2, 3, 4, 10, 12}


#union
print(nums1.union(nums2)) #ouput {1, 2, 3, 4, 5, 6, 7, 8, 10, 12}

#intersection
print(nums1.intersection(nums2)) #output {5, 6}

nums1.difference_update(nums2)
print(nums1) #ouput {1, 2, 3, 4, 10, 12}

#discard : removes the specified item
nums1.discard(10)
print(nums1) #output {1, 2, 3, 4, 12}

#remove : removes the specified element, raises erroe if element not present
nums1.remove(12)
print(nums1) #output {1, 2, 3, 4}

#sysmmetric_difference : Return a set that contains all items from both sets, except items that are present in both sets:
x = {'apple', 'mango', 'cherry'}
y = {'papaya', 'apple'}
z = x.symmetric_difference(y)
print(z) #ouput {'papaya', 'cherry', 'mango'}

#disjoint
letters1 = {'a', 'b', 'c'}
letters2 = {'d', 'e', 'f'}
print(letters1.isdisjoint(letters2)) #output True

#subset
letters3 = {'d', 'e', 'c', 'b', 'a'}
print(letters1.issubset(letters3)) #output True

#superset
print(letters3.issuperset(letters1)) #output True

l=[1.2,1.1,0.9]
l.sort()
print(l)

s=list('abca')
print(s)