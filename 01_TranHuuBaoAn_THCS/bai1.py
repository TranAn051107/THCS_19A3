n = int(input("Nhap vao mot so: "))
i = 0
while i <= n:
    if i*i == n:
        print(f"so {n} la so chinh phuong")
        break
    i = i + 1
else:
    print(f"so {n} khong phai la so chinh phuong")