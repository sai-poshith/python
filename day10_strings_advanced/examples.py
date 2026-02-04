# Check palindrome
word = input("Enter a word: ")

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
# Count vowels
word = input("Enter a word: ").lower()

count = 0
for ch in word:
    if ch in "aeiou":
        count += 1

print("Vowel count:", count)
# Count spaces
sentence = input("Enter a sentence: ")

count = 0
for ch in sentence:
    if ch == " ":
        count += 1

print("Spaces:", count)
# Reverse string using loop
word = input("Enter a word: ")

reverse = ""
for ch in word:
    reverse = ch + reverse

print("Reversed:", reverse)
# Count frequency of a character
word = input("Enter a word: ")
char = input("Enter character to count: ")

count = 0
for ch in word:
    if ch == char:
        count += 1

print("Count:", count)
