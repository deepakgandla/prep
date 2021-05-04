class Student:
    def __init__(self, name, rollNo, m, s):
        self.name = name
        self.rollNo = rollNo
        self.mathScore = m
        self.scienceScore = s
    def totalGrade(self):
        return self.mathScore + self.scienceScore
    def highestScore(self):
        return 'math' if self.mathScore > self.scienceScore else 'science'
    def __str__(self):
        return self.name
s1=Student("Deepak", 68, 95, 90)
s2=Student("John", 69, 90, 90)
s3=Student("Robb", 70, 85, 95)
s4=Student("Jaime", 71, 95, 95)

ls=[s1, s2, s3, s4]

for i in ls:
    print(i.highestScore())
