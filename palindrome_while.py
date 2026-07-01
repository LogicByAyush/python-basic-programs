#palindrome number 
num = int(input("Enter the number: ")) 
rev = 0

while num > 0:
    last = num % 10
    rev = rev * 10 + last
    num = num // 10
 
if rev == num:
    print("palindrome number")
else:
    print("Not palindrome number")