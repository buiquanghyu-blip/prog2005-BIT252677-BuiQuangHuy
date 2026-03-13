class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

student1 = Student("Huy", 10)
student2 = Student("Hưng", 8.5)

print("Sinh viên 1:", student1.name, "-", student1.score)
print("Sinh viên 2:", student2.name, "-", student2.score)
