def count_vowels(s):
    vowels = "aeiou"
    count = 0

    for char in s.lower():
        if char in vowels:
            count += 1

    return count


text = input("Nhập một chuỗi: ")
print("Số chữ nguyên âm là:", count_vowels(text))
