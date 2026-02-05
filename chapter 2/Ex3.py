n = int(input("Nhập số n: "))

if n <= 0:
    print("Vui lòng nhập số nguyên dương!")
else:
    a, b = 0, 1
    print("Dãy Fibonacci:")

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
