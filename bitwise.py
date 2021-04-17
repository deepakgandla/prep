n=int(input())

bi=bin(n)

bi=int(bi[2:])

x=[]

while(bi>0):

    x.append(bi%10)

    bi//=10


a=x.count(1)

b=x.index(1)

x.reverse()

c=len(x)-x.index(1)-1

print(a,b,c,sep="#")
