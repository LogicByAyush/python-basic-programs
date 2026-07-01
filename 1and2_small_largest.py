size = 10
number = []

print(f"Enter {size} elements")
for i in range(size):
    num = int(input(f"Enter {i+1} element: "))
    number.append(num)

larg = sec_larg = float("-inf")
smal = sec_smal = float("inf")

for num in number:
    if num > larg:
        sec_larg = larg
        larg = num
    elif num == larg:
        sec_larg = num
    elif num > sec_larg:
        sec_larg = num
    if num < smal:
        sec_smal = smal
        smal = num
    elif num == smal:
        sec_smal = num
    elif num < sec_smal:
        sec_smal = num

print(f"Largest number {larg} \nSmallest number {smal} \nSecond largest number {sec_larg} \nSecond smallest number {sec_smal}")