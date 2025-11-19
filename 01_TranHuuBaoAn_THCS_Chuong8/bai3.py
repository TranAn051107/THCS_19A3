a = int(input("Nhập tử số :"))
b = int(input("Nhập mẫu số :"))
while b == 0:
    b = int(input("Mẫu phải khác 0 , nhập lại: "))
dau = 1
if a * b < 0:
    dau = -1
a = abs(a)
b = abs(b)
ucln = 1
i = 1
while i <= a and i <= b:
    if a % i == 0 and b % i == 0:
         ucln = i
    i += 1
tu = int(a // ucln) * dau
mau = int(b // ucln)
print(f"Phân số tối giản của {a} / {b} là:" , tu ,"/", mau)