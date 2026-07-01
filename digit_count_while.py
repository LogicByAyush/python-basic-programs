#Count_Digits_While.py
num = int(input("Enter the number: "))
count = 0
number = abs(num)

while number > 0:
    count += 1
    number = number//10

if num == 0:
    print("The number 0 is having 1 digits.")
else:
    print(f"The number {num} is having {count} digits.")