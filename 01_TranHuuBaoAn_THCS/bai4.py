n = int(input("Nhập vào n: "))
print(f"Các số nguyên tố nhỏ hơn {n} là: ", end= " ")
a = 2
while a < n:
    i = 2
    So_Nguyen_To = True
    while i < a:
        if a % i == 0:
            So_Nguyen_To = False
            break
        i += 1
    if So_Nguyen_To:
        print(a, end=" ")
    a += 1