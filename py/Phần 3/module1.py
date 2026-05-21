def cong(a, b): return a + b
def tru(a, b): return a - b
def nhan(a, b): return a * b
def chia(a, b): return a / b
x = int(input("Nhap so thu nhat: "))
y = int(input("Nhap so thu hai: "))
print("Tong 2 so la: ", cong(x, y))
# Minh dien them cac phep tinh con thieu theo mau cua ban
print("Hieu 2 so la: ", tru(x, y))
print("Tich 2 so la: ", nhan(x, y))
print("Thuong 2 so la: ", chia(x, y))
