def maxSub(arr):
    max_so_far=arr[0]
    curr_max=arr[0]
    for i in range(1,len(arr)):
        curr_max=max(arr[i], curr_max+arr[i])
        max_so_far=max(curr_max, max_so_far)
    return max_so_far
print(maxSub([-2, -3, 4, -1, -2, 1, 5, -3] ))
