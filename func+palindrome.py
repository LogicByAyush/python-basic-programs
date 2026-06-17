def is_palindrome(text):
    text = text.lower()

    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True

text = input("Enter the text: ")
print(f"{text} is a palindrome: {is_palindrome(text)}")