import math

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))

power = a ** b

sqrt_a = math.sqrt(a)

div_int = a // b

mod = a % b

round_a = round(a)
round_b = round(b)

print("a^b =", power)
print("Căn bậc 2 của a =", sqrt_a)
print("Chia lấy phần nguyên a // b =", div_int)
print("Chia lấy phần dư a % b =", mod)
print("Làm tròn a =", round_a)
print("Làm tròn b =", round_b)
