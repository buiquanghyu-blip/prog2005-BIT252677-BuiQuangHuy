try:
    a = int(input("Nhập số nguyên thứ nhất: "))
    b = int(input("Nhập số nguyên thứ hai: "))

    result = a / b
    print(f"Kết quả phép chia: {result}")

except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0.")

except ValueError:
    print("Lỗi: Vui lòng nhập số nguyên hợp lệ.")
