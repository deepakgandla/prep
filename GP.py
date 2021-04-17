def printGP(a, r, n):
    for i in range(0, n):
        current_num = a*pow(r, i)
        print(current_num, end=" ")
        
printGP(4, 2, 10)
