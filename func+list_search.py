def search(nums, target):

    for i in range(len(nums)):
        if nums[i] == target:
            return True
    return False

numbers = []
print("Enter 5 numbers: ")

for i in range(5):
    number = int(input(f"Enter {i+1} number: "))
    numbers.append(number)

find = int(input("Enter the number you want to find: "))
print(f"{find} is in the list: {search(numbers, find)}")