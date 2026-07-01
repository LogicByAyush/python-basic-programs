#reverse numbere
num = int(input("Enter the number: "))
number = num
rev = 0

while num > 0:
    last = num % 10
    rev = rev * 10 + last
    num = num // 10

print(f"Revers of {number} is {rev}")