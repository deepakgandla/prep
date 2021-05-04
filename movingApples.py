def moving(n, arr):
	avg = sum(arr)//n
	result = 0
	for i in range(n):
		result += abs(avg-arr[i])
	return result//2
print(moving(5, [2849, 1620, 705, 1, 30]))
