can_nang = float(input("Nhập cân nặng (kg): "))
chieu_cao = float(input("Nhập chiều cao (m): "))
bmi = round(can_nang / (chieu_cao * chieu_cao), 2)
print("Chỉ số BMI của bạn là:", bmi)