# Vi du 2: Class DaySoThuc
class DaySoThuc:
    def __init__(self):
        self.n = 0
        self.danh_sach = []
        
    def nhap_du_lieu(self):
                self.n = int(input("Nhap so luong phan tu n = "))
        for i in range(self.n):
            gia_tri = float(input("Nhap phan tu thu " + str(i + 1) + ": "))
            self.danh_sach.append(gia_tri)
ds = DaySoThuc()
ds.nhap_du_lieu()
print("Danh sach vua nhap la:", ds.danh_sach)
