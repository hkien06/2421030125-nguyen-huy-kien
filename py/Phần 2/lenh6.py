# giai pt bac nhat: ax + b = 0
a = float(input("Nhap he so a: "))
b = float(input("Nhap he so b: "))

if a == 0:
    if b == 0:
        print("Phuong trinh vo so nghiem")
    else:
        print("Phuong trinh vo nghiem")
else:
    x = -b / a
    print("Nghiem cua phuong trinh la x =", x)
