a = int(input("Nhập vào số thứ nhất:"))
c = int(input("Nhập vào số thứ hai:"))
while a != c:
    if a > c:
        a = a - c
    else:
        c = c - a
print(f"Ước chung lớn nhất {a}và{c} là:",a)