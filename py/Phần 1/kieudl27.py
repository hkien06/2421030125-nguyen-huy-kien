# Truy cap phan tu cua list 2 chieu
print(lst[0])       # In ra list con dau tien: [1, 2, 3]
print(lst[1])       # Hoac lst[-1], in ra: [4, 5, 6]
print(lst[0][0])    # In ra phan tu dau tien cua list con dau tien: 1
print(lst[1][1])    # In ra phan tu thu hai cua list con thu hai: 5
# Cat list con
print(lst[0][:2])   # In ra: [1, 2]
print(lst[1][:])    # In ra: [4, 5, 6]
tup = (1, 2, 3, 4)
print(tup)
tup = (1, 2, 3, 4)
# Khoi tao tuple rong
e_tup = () 
print(e_tup)
# Tuple chua tuple khac va list
tup2 = ((1, 2, 3), [4, 5])
print(tup2[0])      # Tra ve: (1, 2, 3)
print(tup2[0][2])   # Tra ve: 3
print(tup2[1][0])   # Tra ve: 4