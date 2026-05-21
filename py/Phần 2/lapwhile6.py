# btvn: nhap vao 1 day so khac 0. Tinh tong cac so chan
tong_chan = 0
while True:
    so = int(input("Nhap vao 1 so nguyen (nhap 0 de dung): "))
    if so == 0:
        break     
    if so % 2 == 0:
        tong_chan += so
print("Tong cac so chan da nhap la:", tong_chan)
