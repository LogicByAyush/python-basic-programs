number = []
count = 0

elem = int(input("Enter the size of list: "))
print(f"Enter {elem} elements in list")

for i in range(elem):
    num = int(input(f"Enter {i+1} element: "))
    number.append(num)

find = int(input("Enter the number for counting frequency: "))

for num in number:
    if find == num:
        count += 1

print(f"{find} appears {count} times")

if count == 0:
    print("Number not found")