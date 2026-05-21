# viet chg trinh nhap 1 day so nguyen gom n ptu. Tinh va in ra tong
a = []
s = 0
n = int(input("Nhap so ptu cua dso: "))
for i in range(1, n + 1):
    k = int(input("Nhap phan tu thu " + str(i) + ": "))
    a.append(k)
for i in a:
    s = s + i
print("Tong cua day so la: " + str(s))
