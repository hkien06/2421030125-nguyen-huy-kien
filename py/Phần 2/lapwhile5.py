# nhap vao 3 diem toan, ly, hoa va tinh diem tb, xep loai
toan = float(input("Nhap vao diem toan: "))
ly = float(input("Nhap vao diem ly: "))
hoa = float(input("Nhap vao diem hoa: "))
dtb = (toan + ly + hoa) / 3
if (dtb < 5):
    print("yeu")
elif (dtb < 7):
    print("tb")
elif (dtb < 9):
    print("kha")
elif (dtb <= 10):
    print("gioi")
