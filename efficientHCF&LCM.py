def eucRechcf(x, y):
    ''' euclidean using recursion '''
    if y == 0:
        return x
    return eucRechcf(y, x%y)

def eucHcf(x, y):
    ''' euclidean without recursion '''
    while(y):
        x, y = y, x%y
    return x

def lcm(x, y):
    ''' product of x and y is equal to product of lcm(x, y) and hcf(x, y) i.e., x*y=lcm(x, y) * hcf(x, y)'''
    product = x*y
    hcf = eucHcf(x, y)
    return product // hcf

print('hcf with recursion {}, hcf without recursion {}'.format(eucRechcf(54, 24), eucHcf(54, 24)))
print('lcm {}'.format(lcm(50, 20)))
