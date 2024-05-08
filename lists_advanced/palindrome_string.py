def is_palindrome(word):
    if word[::-1] == word:
        return word


words = input().split(" ")
palindrome = input()
palindrome_list = [word for word in words if is_palindrome(word)]
palindrome_counter = 0
for element in palindrome_list:
    if element == palindrome:
        palindrome_counter += 1

print(palindrome_list)
print(f"Found palindrome {palindrome_counter} times")