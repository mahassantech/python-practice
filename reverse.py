word = input("Enter a word: ")

reverse_word = word[::-1]

print(reverse_word)

word = input("Enter a word: ")
reverse_word = ""

for ch in word:
    reverse_word = ch + reverse_word

print(reverse_word)