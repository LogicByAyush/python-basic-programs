def second_largest(nums):
    first = nums[0]

    for num in nums:
        if num > first:
            first = num

    count = 0
    second = None

    for num in nums:
        if num == first:
            count += 1

    if count >= 2:
        return first

    for num in nums:
        if num != first:
            second = num
            break

    for num in nums:
        if num != first and num > second:
            second = num

    return second

number = []
elem = int(input("Enter the size of list: "))
print(f"Enter {elem} elements of list")

for i in range(elem):
    nums = int(input(f"enter {i+1} element: "))
    number.append(nums)

print(f"The second larges number among list is {second_largest(number)}")