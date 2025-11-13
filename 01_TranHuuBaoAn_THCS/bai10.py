luong_co_ban = float(input("Nhập mức lương cơ bản (VNĐ): "))
ngay_cong = int(input("Nhập số ngày công trong tháng: "))
luong_ngay = luong_co_ban / 22
luong_tong = luong_ngay * ngay_cong
thuong = luong_tong * 0.10 * (ngay_cong > 22)
phat = luong_tong * 0.05 * (ngay_cong < 22)
luong_thuc_nhan = luong_tong + thuong - phat
print("Tổng lương thực nhận là: {:.2f} VNĐ".format(luong_thuc_nhan))
