import random

m = int(input("Nhập số hàng M: "))
n = int(input("Nhập số cột N: "))

matrix = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(random.randint(1, 100))
    matrix.append(row)

print("Ma trận:")
for row in matrix:
    print(row)

r = int(input("Nhập số hàng muốn hiển thị (bắt đầu từ 1): "))
print("Hàng", r, ":", matrix[r-1])

c = int(input("Nhập số cột muốn hiển thị (bắt đầu từ 1): "))
print("Cột", c, ":")
for i in range(m):
    print(matrix[i][c-1])

max_val = matrix[0][0]
for row in matrix:
    for val in row:
        if val > max_val:
            max_val = val

print("Giá trị lớn nhất trong ma trận:", max_val)
