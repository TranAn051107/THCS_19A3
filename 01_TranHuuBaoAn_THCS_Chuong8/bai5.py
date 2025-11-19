n = int(input("Nhập vào n :"))
S1 = 0
for i in range (1,n+1):
    S1 += i
print("S1 =",S1)

n = int(input("Nhập vào n :"))
S2= 1
for i in range (1,n):
    S2 *= i
print("S2=",S2)

n = int(input("Nhập vào n :"))
S3= 0
for i in range (1,n+1):
    S3 += ((-1)**(i + 1)) / i
print("S3= ", S3)

n = int(input("Nhập vào n :"))
S4 = 0
for i in range(0, n + 1):
    S4 += i / (i + 2)
print("S4 =", S4)
