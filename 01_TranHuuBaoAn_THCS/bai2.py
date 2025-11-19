a = int(input(" nhap vao so thu nhat: "))
b = int(input("nhap vao so thu hai: "))
while a != b:
    if a > b:
        a = a - b
    else :
        b = b - a
print(f"Uoc chung lon nhat của {a} va {b} la: ", a)