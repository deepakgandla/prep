def lds(arr, n):
  
    lds = [1] * n


    for i in range(1, n):
        for j in range(i):
            if (arr[i]<arr[j] and lds[i]<lds[j]+1):
                lds[i]=lds[j]+1
    
    return max(lds)
  
      
arr = [ 15, 27, 14, 38, 63, 55, 46, 20, 10, 5, 65, 85 ]
n = len(arr)
print("Length of LDS is", lds(arr, n))
