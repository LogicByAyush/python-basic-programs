text = input("Enter the text: ")
n = len(text)
rev = ""

for i in range(n-1, -1, -1):
    rev += text[i]

print(f"reverse of ({text}) is ({rev})")