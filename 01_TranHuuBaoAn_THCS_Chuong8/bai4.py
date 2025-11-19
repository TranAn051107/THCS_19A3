n = int(input("Nhập vào n: "))
print(f"Các số nguyên tố nhỏ hơn {n} là: ", end=" ")
i = 2
while i < n:
    j = 2
    SoNguyenTo = True
    while j < i:
        if i % j == 0:
            SoNguyenTo = False
            break
        j += 1
    if SoNguyenTo:
        print(i, end=" ")
    i += 1