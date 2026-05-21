n = int(input("Nhap n: "))
tich = 1
m = n

while m > 0:
    tich = tich * (m % 10)
    tam = m // 10

print("Tich cac chu so =", tich)

if tich % 2 == 0 and tich > 20:
    print("True")
else:
    print("False")