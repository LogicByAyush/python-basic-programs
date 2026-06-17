nums = []
total = 0
element = int(input("Enter the number of element you want to add on list: "))
print(f"Enter {element} numbers:")

for i in range(element):
    num = int(input())
    nums.append(num)
    total += num

avg = total / element

print("List =", nums)
print("Sum =", total)
print("Average =", avg)