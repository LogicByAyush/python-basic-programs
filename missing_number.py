#Missing_Number.py
total = 0
num_total = 0

n = int(input("Enter N: "))

for i in range(n):
    total += i+1

print(f"Enter elements: ")

for i in range(n-1):
    num = int(input())
    num_total += num

missing_num = total - num_total
print(f"Missing number is {missing_num}.")