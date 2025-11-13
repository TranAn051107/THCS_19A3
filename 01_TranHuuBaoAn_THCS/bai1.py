gia_san_pham = float(input("Nhập giá sản phẩm: "))
so_luong = int(input("Nhập số lượng sản phẩm: "))
tong_chi_phi = gia_san_pham * so_luong
vat = tong_chi_phi * 0.1
tong_tien = tong_chi_phi + vat
print("Tổng tiền phải trả: {:.2f} ".format(tong_tien))