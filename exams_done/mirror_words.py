import re

text = input()

regex = r"([@#])([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"

match = re.findall(regex, text)

palindrome_words = []

for pair in match:
    if pair[1] == pair[2][::-1]:
        palindrome_words.append(f"{pair[1]} <=> {pair[2]}")

if not match:
    print("No word pairs found!")
else:
    print(f"{len(match)} word pairs found!")

if not palindrome_words:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(palindrome_words))

