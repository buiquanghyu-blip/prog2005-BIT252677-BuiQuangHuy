numbers = list(map(int, input("Nhập các số nguyên cách nhau bởi dấu cách: ").split()))

swap_count = 0
n = len(numbers)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swap_count += 1

print("Danh sách sau khi sắp xếp tăng dần:", numbers)
print("Số lần hoán đổi:", swap_count)
