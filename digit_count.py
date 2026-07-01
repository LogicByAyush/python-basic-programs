#digit_count
def digit_count(num):
    if num == 0:
        return 0
    return 1 + digit_count(num//10)

number = int(input("Enter the number: "))
if number == 0:
    print("The number 0 is having 1 digits.")
elif number > 0:
    print(f"The number {number} is having {digit_count(number)} digits.")
else:
    print("Enter positive number")