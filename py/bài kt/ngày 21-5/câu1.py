n = int(input("Nhap n: "))
tong = 0
dem = 0
for i in range(n):
    x = float(input("Nhap so thu " + str(i + 1) + ": "))
    if x > 0 and x < 1000:
        tong = tong + x
        dem = dem + 1
if dem > 0:
    print("Trung binh cong =", tong / dem)
else:
    print("Khong co so hop le")