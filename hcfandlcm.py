def hcf(a, b):
    if a < b:
        smaller = a
    else:
        smaller = b
    for i in range(1, smaller+1):
        if (a % i == 0) and (b %i == 0):
            hcf = i
    return hcf

def lcm(a, b):
    if  a > b:
        greater = a
    else:
        greater = b
    while(True):
        if (greater % a== 0) and (greater % b == 0):
            return greater
        greater+=1

print('hcf : {}'.format(hcf(16, 4)))
print('lcm : {}'.format(lcm(54, 24)))

