def divsion():
    total_students = int(input())
    if total_students < 100 or total_students > 200:
        print("INVALID OUPUT")
    elif total_students % 4 == 0:
        for i in range(4):
            print(total_students//4)
    elif total_students % 2 != 0:
        a= total_students
        while total_students:
            if total_students % 4 == 0:
                new_total = total_students
                break
            total_students -=1
        for i in range(3):
            print(new_total//4)
        diff = a - new_total 
        print((new_total//4) + diff)
divsion()
