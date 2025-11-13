tong_keo =int(input("nhap tong so keo: "))
so_hoc_sinh = int(input("nhap so hoc sinh: "))
keo_moi_hs = tong_keo // so_hoc_sinh
keo_con_thua = tong_keo % so_hoc_sinh
print("moi hoc sinh nhan duoc:", keo_moi_hs, "keo")
print("so keo con thua:", keo_con_thua, "cai")