n = int(input("Nhap n: "))
tong = 0
m = n
while m > 0:
    tong = tong + m % 10
    tam = m // 10
print("Tong cac chu so =", tong)
if tong % 3 == 0:
    print("Chia het cho 3")
else:
    print("Khong chia het cho 3")