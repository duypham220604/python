import math

#kiem tra bang cach can bac 2 gia tri n sau do mu 2 len xem co bang gia tri n khong
sochinhphuong = lambda n: math.sqrt(n) ** 2 == n
n = int(input("nhap n: "))
if sochinhphuong(n):
    print(f"{n} la so chinh phuong")
else:
    print(f"{n} khong phai so chinh phuong")

a = int(input("\nNhap canh a: "))
b = int(input("Nhap canh b: "))
c = int(input("Nhap canh c: "))

tam_giac = lambda a, b, c: (
    a + b > c and
    a + c > b and
    b + c > a
)

if tam_giac(a, b, c):

    if a == b == c:
        print("Tam giac deu")

    elif a == b or a == c or b == c:

        if (
            a*a + b*b == c*c or
            a*a + c*c == b*b or
            b*b + c*c == a*a
        ):
            print("Tam giac vuong can")
        else:
            print("Tam giac can")

    elif (
        a*a + b*b == c*c or
        a*a + c*c == b*b or
        b*b + c*c == a*a
    ):
        print("Tam giac vuong")

    else:
        print("Tam giac thuong")

else:
    print("Khong phai tam giac")
