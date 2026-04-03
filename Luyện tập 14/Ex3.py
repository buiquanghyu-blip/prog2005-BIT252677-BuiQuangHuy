import math

n = int(input("Nhập số phần tử: "))
arr = []

for i in range(n):
    x = int(input(f"Nhập phần tử {i+1}: "))
    arr.append(x)

so_le = [x for x in arr if x % 2 != 0]
print("Các số lẻ:", so_le)
print("Số lượng số lẻ:", len(so_le))

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

so_nguyen_to = [x for x in arr if is_prime(x)]
print("Các số nguyên tố:", so_nguyen_to)
