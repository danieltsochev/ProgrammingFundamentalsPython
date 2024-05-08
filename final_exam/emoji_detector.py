import re

text = input()
regex = r"(\:{2}|\*{2})([A-Z][a-z]{2,})\1"
matches = re.findall(regex, text)

numbers = []
cool_threshold = 1
for element in text:
    if element.isdigit():
        numbers.append(int(element))
for number in numbers:
    cool_threshold *= number

names = []
for match in matches:
    names.append(match[1])

cool_emojis = []
for name in names:
    emoji_threshold = 0
    for letter in name:
        emoji_threshold += ord(letter)
    if emoji_threshold > cool_threshold:
        cool_emojis.append(name)

cool_emojis_total = []

for couple in matches:
    if couple[1] in cool_emojis:
        cool_emojis_total.append(f"{couple[0]}{couple[1]}{couple[0]}")

print(f"Cool threshold: {cool_threshold}")
print(f"{len(matches)} emojis found in the text. The cool ones are:")
for emoji in cool_emojis_total:
    print(emoji)