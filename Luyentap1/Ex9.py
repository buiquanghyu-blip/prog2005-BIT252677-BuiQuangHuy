class Student:
    def __init__(self, name, score):
        self.name = name

        if 0 <= score <= 10:
            self.score = score
        else:
            print("Điểm không hợp lệ! Điểm phải từ 0 đến 10.")
            self.score = 0

    def display(self):
        print(f"Sinh viên {self.name} có điểm là {self.score}")


student1 = Student("A", 10)
student2 = Student("B", 8)

student1.display()
student2.display()
