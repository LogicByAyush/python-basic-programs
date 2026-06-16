num = int(input("Enter number: "))
count = 0

for i in range(2, num + 1, 2):
    count += 1

print(f"Total even numbers = {count}")