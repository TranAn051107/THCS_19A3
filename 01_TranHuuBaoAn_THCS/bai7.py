ten_dang_nhap = input("Nhập tên đăng nhập: ")
mat_khau = input("Nhập mật khẩu: ")
quyen_truy_cap = (ten_dang_nhap == "admin") and (mat_khau != "password123")
print("Quyền truy cập:", quyen_truy_cap)