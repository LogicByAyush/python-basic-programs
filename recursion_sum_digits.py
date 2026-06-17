# recursion_sum_digits
def dig_sum(num):
    if num == 0:
        return 0
    return num % 10 + dig_sum(num//10)

number = int(input("Enter the number: "))
print(f"Digit sum of {number} is {dig_sum(number)}")