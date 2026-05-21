import math
def dien_tich_hinh_tron(r):
    return math.pi * r * r
def dien_tich_hinh_chu_nhat(a, b):
    return a * b
def dien_tich_hinh_vuong(a):
    return a ** 2
def chu_vi_hinh_chu_nhat(a, b):
    return (a + b) * 2
chieu_dai = int(input("Chieu dai hcn la: "))
chieu_rong = int(input("Chieu rong hcn la: "))
print("Dien tich hinh chu nhat la: ", dien_tich_h_chu_nhat(chieu_dai, chieu_rong))
print("Chu vi hinh chu nhat la: ", chu_vi_h_chu_nhat(chieu_dai, chieu_rong))
