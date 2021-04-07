#transpose of a matrix
lst=[[1,2],[3,4],[5,6]]
result=[[lst[j][i] for j in range(len(lst))] for i in range(len(lst[0]))]
#adding matrices
a1=[[1,2,3],
    [1,2,3],
    [3,4,5]]
a2=[[8,3,4],
    [2,3,4],
    [1,6,5]]
result=[[a1[i][j]+a2[i][j] for j in range(len(a1[0]))] for i in range(len(a1))]
#mutiplication matrices
a3=[[1,2,3],
    [4,5,6]]
a4=[[7,8],
    [9,10],
    [11,12]]
result=[[0,0],
        [0,0]]
for i in range(len(a3)):
    for j in range(len(a4[0])):
                   for k in range(len(a4)):
                       result[i][j]+=a3[i][k]*a4[k][j]

result=[[sum(a*b for a,b in zip(x,y)) for y in zip(*a4)] for x in a3]
for x in a3:
    for y in zip(*a4):
        for a,b in zip(x,y):
            print(a,b)

v='aeiou'
s='aheybjk  uhiausgd Lahudhao'
dc={}
for i in s:
   if i in v:
       if i in dc:
           dc[i]+=1
       else:
            dc[i]=1
n=2345
rn=0
while n>0:
    
    remainder=n%10
    rn=rn*10+remainder
    n=n//10

import numpy as np

array = np.random.rand(2, 2, 2, 2)
print(array)
print(array[..., 0])
print(array[Ellipsis, 0])