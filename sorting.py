nums=[8,1,9,4,2]
for i in range(len(nums)-1,0,-1):
    for j in range(i):
        if nums[j]>nums[j+1]:
            temp=nums[j]
            nums[j]=nums[j+1]
            nums[j+1]=temp


nums2=[5,4,3,1,2]
for i in range(len(nums2)):
    minpos=i
    for j in range(i,len(nums2)):
        if nums2[j]<nums2[minpos]:
            minpos=j

    temp=nums2[i]
    nums2[i]=nums2[minpos]
    nums2[minpos]=temp


def binsrch(nums3,item):
    low=0
    high=len(nums3)-1
   
    while low<high:
        mid=(low+high)//2
        if nums3[mid]==item:
            return mid
        elif nums3[mid]<item:
            low=mid
            
        else:
            high=mid
nums3=[1,2,3,4,5]
#print(binsrch(nums3,4))
      
            
            
x=globals()
print(x["__file__"])
print(x["__doc__"])
print(x["__name__"])
print(x["__builtins__"])