a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
tong = a + b
print("Tong =", tong)

max = 0
n = tong

while n > 0:
    n = n % 10

    if n > max:
        max = n

    n = n // 10

print("Chu so lon nhat =", max_cs)