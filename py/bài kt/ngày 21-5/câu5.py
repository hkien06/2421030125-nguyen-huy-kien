m = int(input("Nhap m: "))
n = int(input("Nhap n: "))
tong = 0
i = n

while i > 0:
    tong = tong + i % 10
    i = i // 10

print("Tong cac chu so cua n =", tong)

if m % tong == 0:
    print("m chia het")
else:
    print("m khong chia het")