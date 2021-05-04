def selectionSort(array):
	n = len(array)
	for i in range(n):
		minPos = i
		for j in range(i+1, n):
			if array[j] < array[minPos]:
				minPos = j
		array[i], array[minPos] = array[minPos], array[i]
	return array
#print(selectionSort([24, 1, 2]))

def bubbleSort(array):
	n = len(array)
	for i in range(n):
		for j in range(0, n-i-1):
			if array[j] > array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]
	return array

#print(bubbleSort([7, 5, 3, 9, 1, 2]))

def insertionSort(array):
	n = len(array)
	for i in range(n):
		current = array[i]
		j = i-1
		while j>=0 and array[j] > current:
			array[j+1] = array[j]
			j -=1
		array[j+1] = current
	return array
#print(insertionSort([7, 5, 3, 8, 1]))

def mergeSort(array):
	if len(array) > 1:
		mid = len(array)//2
		L = array[:mid]
		R = array[mid:]
		mergeSort(L)
		mergeSort(R)
		i=j=k=0
		while i<len(L) and j<len(R):
			if L[i] < R[j]:
				print(array)
				array[k] = L[i]
				i = i+1
			else:
				array[k] = R[j]
				j = j+1
			k = k+1
		while i<len(L):
			array[k] = L[i]
			i = i+1
			k = k+1
		while j<len(R):
			array[k] = R[j]
			j = j+1
			k = k+1
	return array
#print(mergeSort([7, 5, 20, 4,45, 3]))



def partition(array, start, end):
	print(end)
	pivot =array[end]
	pIndex = start
	for i in range(0, end):
		if array[i] <= pivot:
			array[i], array[pIndex] = array[pIndex], array[i]
			pIndex += 1
			print(pIndex)
	array[pIndex], array[end] = array[end], array[pIndex]
	return pIndex
def quickSort(array, start, end):
	if start < end:
		pIndex = partition(array, start, end)
		print(pIndex)
		quickSort(array, start, pIndex-1)
		quickSort(array, pIndex+1, end)

l = [2, 9, 1 ,7 ,8]
quickSort(l, 0, len(l)-1)
print(l)
