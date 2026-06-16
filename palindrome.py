def is_palindrome(n):
    return str(n) == str(n)[::-1]

text = input("Enter a number or text for checking palindrome: ")
text = text.lower()
print(f"The input {text} is {'a palindrome' if is_palindrome(text) else 'not a palindrome'}.")