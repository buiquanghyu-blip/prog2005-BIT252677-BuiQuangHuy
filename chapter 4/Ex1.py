def thong_ke_tuple(t):
    tong = sum(t)
    lon_nhat = max(t)
    nho_nhat = min(t)

    return tong, lon_nhat, nho_nhat

data = (3, 6, 3, 6, 1, 8, 9)

tong, lon_nhat, nho_nhat = thong_ke_tuple(data)

print("Tổng:", tong)
print("Giá trị lớn nhất:", lon_nhat)
print("Giá trị nhỏ nhất:", nho_nhat)
