s1 = input("Nhập chuỗi s1: ")
s2 = input("Nhập chuỗi s2: ")
s3 = input("Nhập chuỗi s3: ")
index = int(input("Nhập index: "))

len_s1 = len(s1)
len_s2 = len(s2)
len_s3 = len(s3)

s4 = s1[index:]

s2_repeated = s2 * 2

print("Chiều dài chuỗi s1 =", len_s1)
print("Chiều dài chuỗi s2 =", len_s2)
print("Chiều dài chuỗi s3 =", len_s3)
print("Chuỗi s4 =", s4)
print("Chuỗi s2 lặp lại 2 lần =", s2_repeated)