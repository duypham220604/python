import math

# Lambda kiem tra so chinh phuong
sochinhphuong = lambda n: math.sqrt(n) ** 2 == n
# Lambda kiem tra so hoan thien
sohoanthien = lambda n: (
    sum(i for i in range(1, n) if n % i == 0) == n
)

# Liet ke tu 1 -> 10000

print("Cac so chinh phuong tu 1 den 10000:")

for i in range(1, 10001):
    if sochinhphuong(i):
        print(i, end=" ")

print("\n")

print("Cac so hoan thien tu 1 den 10000:")

for i in range(1, 10001):
    if sohoanthien(i):
        print(i, end=" ")