def sqrGen():
    n = 1
    while n <= 10:
        yield n*n
        n += 1

values = sqrGen()
print(values.__next__())
print(values.__next__())
