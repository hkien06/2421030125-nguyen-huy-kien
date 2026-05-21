# Yeu cau: Nhap vao 2 so x, y. Kiem tra xem x = y, x > y, x < y

# Cach 1: Su dung cac lenh if doc lap
print("--- Cach 1 ---")
x = float(input("Nhap x: "))
y = float(input("Nhap y: "))
if (x > y):
    print(x, "lon hon", y)
if (x < y):
    print(x, "nho hon", y)
if (x == y):
    print(x, "bang", y)
# Cach 2: Su dung if else long nhau
print("\n--- Cach 2 ---")
x = int(input("Nhap x: "))
y = int(input("Nhap y: "))
if (x > y):
    print("x lon hon y")
else:
    if (x == y):
        print("x bang y")
    else:
        print("x nho hon y")
