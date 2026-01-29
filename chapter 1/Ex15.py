def nhap_diem(mon):
    while True:
        try:
            diem = float(input(f"Nhập điểm {mon}: "))
            if 0 <= diem <= 10:
                return diem
            else:
                print("Điểm phải nằm trong khoảng từ 0 đến 10.")
        except ValueError:
            print("Vui lòng nhập số hợp lệ.")

for i in range(1, 4):
    print(f"\n Nhập thông tin sinh viên {i} ")
    ten = input("Nhập tên sinh viên: ")

    toan = nhap_diem("Toán")
    ly = nhap_diem("Lý")
    hoa = nhap_diem("Hóa")

    diem_tb = (toan + ly + hoa) / 3

    print(f"Sinh viên: {ten}")
    print(f"Điểm trung bình: {diem_tb:.2f}")
