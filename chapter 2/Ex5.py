chuoi = input("Nhập một chuỗi: ")
ky_tu = input("Nhập một ký tự: ")

dem = 0
for ch in chuoi:
    if ch == ky_tu:
        dem += 1

print(f"Ký tự '{ky_tu}' xuất hiện {dem} lần trong chuỗi.")
