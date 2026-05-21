# nhap vao 1 day n. hay viet ra va tinh giai thua cua n
def giai_thua(m):
    gt = 1
    for i in range(1, m + 1):
        gt = gt * i
    return gt
n = int(input("Nhap vao 1 so nguyen dg : "))
print("%d! = %d" % (n, giai_thua(n)))
