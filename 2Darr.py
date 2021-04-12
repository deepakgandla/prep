#Different ways of taking input values for 2D array
size = int(input())
x = []
for i in range(size):
    x.append(list(map(int, input("Enter row values space-sep").split())))


size = int(input())
y = []
for i in range(size):
    y.append([int(a) for a in input("Enter row values space-sep").split()])
print(x)
print(y)
