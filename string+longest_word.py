text = input("Enter the text: ")
word = ""
long_word = ""

for ch in text:
    if ch == " ":
        word = ""
    else:
        word += ch
    if len(word) > len(long_word):
        long_word = word

print(f"longest = {long_word}")