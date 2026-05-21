# vi du : 
import datetime
now = datetime.datetime.now()
print(now)
s = now.strftime("%d/%m/%Y, %H:%M:%S")
print("s: ", s)
from datetime import datetime
dt_string = "11/07/2021" 
ngay_thang = datetime.strptime(dt_string, "%d/%m/%Y")
print(ngay_thang)
# Chuyen nguoc lai tu datetime thanh chuoi
s = ngay_thang.strftime("%d/%m/%Y")
print(s)
