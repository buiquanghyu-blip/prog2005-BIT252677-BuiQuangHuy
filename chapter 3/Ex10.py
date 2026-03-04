numbers = list(map(int, input("Nhập các số cách nhau bởi dấu cách: ").split()))

even_numbers = []
even_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
        even_sum += num

print("Các số chẵn trong danh sách:", even_numbers)
print("Tổng các số chẵn là:", even_sum)
