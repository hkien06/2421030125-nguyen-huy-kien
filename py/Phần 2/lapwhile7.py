# vt chg trinh nhap 1 so TN n va tinh cac gt uoc so ngto
n = int(input("Nhap 1 so TN n: "))
dem_uoc_ngto = 0
print("Cac uoc so nguyen to cua", n, "la:")
for i in range(2, n):
    if n % i == 0: # i la uoc cua n       
        la_nguyen_to = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                la_nguyen_to = False
                break
        if la_nguyen_to:
            print(i)
            dem_uoc_ngto += 1
print("Tong so cac uoc so nguyen to khac n la:", dem_uoc_ngto)
