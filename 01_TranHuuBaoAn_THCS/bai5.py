tien_goc = float(input("Nhập số tiền gửi ban đầu (VNĐ): "))
lai_suat_nam = float(input("Nhập lãi suất hàng năm (%): "))
lai_suat = lai_suat_nam / 100
lai_1_thang = tien_goc * lai_suat * (1/12)
lai_2_quy = tien_goc * lai_suat * (2/4)
lai_3_nam = tien_goc * lai_suat * 3
print("Lãi sau 1 tháng: {:.2f} VNĐ".format(lai_1_thang))
print("Lãi sau 2 quý: {:.2f} VNĐ".format(lai_2_quy))
print("Lãi sau 3 năm: {:.2f} VNĐ".format(lai_3_nam))