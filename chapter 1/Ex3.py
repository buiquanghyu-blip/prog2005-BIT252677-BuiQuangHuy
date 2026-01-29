a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))

tong = a + b
hieu = a - b
tich = a * b

if b != 0:
    thuong = a / b
else:
    thuong = "Không thể chia cho 0"

print("Tổng:", tong)
print("Hiệu:", hieu)
print("Tích:", tich)
print("Thương:", thuong)
