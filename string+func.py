def count_v(text):
    vowels = "AEIOUaeiou"
    count = 0

    for ch in text:
        if ch in vowels:
            count += 1
    return count

text = input("Enter the text: ")
print(f"The number of vowels in the text is: {count_v(text)}")