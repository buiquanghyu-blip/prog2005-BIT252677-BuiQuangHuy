numbers = list(map(int, input("Nhập các số cách nhau bởi dấu cách: ").split()))

target = int(input("Nhập số cần tìm: "))

found_index = -1

for i in range(len(numbers)):
    if numbers[i] == target:
        found_index = i
        break

if found_index != -1:
    print("Số", target, "được tìm thấy tại chỉ số:", found_index)
else:
    print("Không tìm thấy số", target, "trong danh sách.")
