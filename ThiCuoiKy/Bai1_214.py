d = float(input("Nhap chieu dai day hinh khoi chu nhat: "))
r = float(input("Nhap chieu rong day hinh khoi chu nhat: "))
h = float(input("Nhap chieu cao hinh khoi chu nhat: "))
sole = int(input("Nhap so le can hien thi: "))

dientichday = d * r # cong thuc tinh dien tich = dai x rong
thetich = d * r * h # cong thuc tinh the tich = dai x rong x cao

print(f"Dien tich day hinh chu nhat: {dientichday:.{sole}f} cm\u00b2")
print(f"The tich hinh khoi: {thetich:.{sole}f} cm\u00b3")