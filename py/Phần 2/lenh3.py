# Yeu cau: Giai phuong trinh bac nhat ax + b = 0
a = float(input("Nhap he so a = "))
b = float(input("Nhap he so b = "))
if (a == 0):
    if (b == 0):
        print("Pt vo so nghiem")
    else:
        print("Pt vo nghiem")
else:
    x = -b / a
    print("x = ", x)
