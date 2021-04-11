
def sum1(n):
    ''' time complexity O(1) '''
    return n * (n+1) //2

def sum2(n):
    ''' time complexity O(n) '''
    total = 0
    for i in range(n+1):
        total = total + i
    return total

n=100000000
print(sum1.__doc__)
print('sum 1', sum1(n))
print('sum 2', sum2(n))
