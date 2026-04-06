def nhap_diem(mon):
    while True:
        d = float(input(f"Nhập điểm {mon}: "))
        if 0 <= d <= 10:
            return d
        print("Điểm không hợp lệ!")

toan = nhap_diem("Toán")
ly = nhap_diem("Lý")
hoa = nhap_diem("Hóa")

dtb = (toan + ly + hoa) / 3
print("DTB:", round(dtb, 2))

if dtb >= 8:
    print("Giỏi")
elif dtb >= 6.5:
    print("Khá")
elif dtb >= 5:
    print("Trung bình")
else:
    print("Yếu")
