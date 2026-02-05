# Character frequency in a string

word = input("Enter a word: ")
freq = {}

for ch in word:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1

print(freq)

# Frequency of numbers in a list

numbers = [1, 2, 2, 3, 1, 4, 2]
freq = {}

for n in numbers:
    if n in freq:
        freq[n] = freq[n] + 1
    else:
        freq[n] = 1

print(freq)
