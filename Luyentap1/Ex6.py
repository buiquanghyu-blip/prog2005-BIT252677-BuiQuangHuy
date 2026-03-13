s = input("Nhập chuỗi số (vd: 5; 7; 8; -2; 8; 11; 13; 9; 10): ")

numbers = [int(x.strip()) for x in s.split(";")]

print("Các số:")
for num in numbers:
    print(num)

even_count = sum(1 for x in numbers if x % 2 == 0)

negative_count = sum(1 for x in numbers if x < 0)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(abs(n)**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_count = sum(1 for x in numbers if is_prime(x))

average = sum(numbers) / len(numbers)

print("Số chẵn:", even_count)
print("Số âm:", negative_count)
print("Số nguyên tố:", prime_count)
print("Giá trị trung bình:", average)
