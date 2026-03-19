vowels=['a','e','i','o','u'] 

word=input('enter your word: ')
count=0
for ch in word: 
    if ch in vowels: 
        count=count+1 
print(count)