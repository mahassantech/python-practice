vowels = ['a','e','i','o','u']

word=input('enter your word: ').lower()
count=0
for char in word:
    if char in vowels:
        count=count+1 
print(count)