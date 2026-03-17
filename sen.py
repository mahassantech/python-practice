word=input('enter your word: ').lower()

words = word.split()
count=0 

for ch in words:
    count=count +1
print(count)