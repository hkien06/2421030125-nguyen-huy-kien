def sum(a, b, p):
    s = a + b
    # Tham so "p" giong nhu 1 mang
    for i in p:
        s = s + i
    return s
print(sum(1, 2))
print(sum(1, 2, 3))
print(sum(1, 2, 4, 5, 6))
