class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def __str__(self):
        return self.name
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        else:
            return False
s1 = Student('Deepak', 78)
s2 = Student('John' ,75)
s3 = Student('Dummy',70)

python = Course('Python', 2)
print(python.add_student(s1))
print(python.add_student(s2))
print(python.add_student(s3))
for i in python.students:
    print(i.name)
