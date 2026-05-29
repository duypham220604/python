#ham kien tra so nguyen to
def isPrime(n):
    if n < 2:
        return False # tra false neu gia tri nho hon 2
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True # tra ve true neu n khong chia lay du duoc

#ham liet ke uoc so
def LietKeUocSo(n):
    list = [] #tao 1 list chua danh sach uoc so
    for i in range(n):
        if isPrime(i) and n % i == 0: # kiem tra dap ung dong thoi 2 dieu kien la so nguyen to va chia duoc cho n
            list.append(i)
    print(f"cac uoc so cua {n} la so nguyen to: {list} ")

#ham thao tac so nguyen to
def SoNguyenTo(num):
    count = 0
    list = []

    #kiem tra so nguyen to
    if isPrime(num):
        print(f"{num} la so nguyen to")
    else:
        print(f"{num} khong phai so nguyen to")

    #dem va in ra danh sach cac so tu nhien < n
    for i in range(num):
        if isPrime(i):
            list.append(i)
            count += 1
    print(f"danh sach cac so nguyen to < {num}: {list}")
    print(f"tong cac so nguyen to be hon {num} la: {count} so")


def main():
    n = int(input("nhap n: "))
    SoNguyenTo(n)
    LietKeUocSo(n)

main()