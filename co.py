user=input('enter your word: ')

vowel =['a', 'e', 'i', 'o', 'u']

count=0

for vo in user:
    if vo in vowel:
        count=count+1 
print(count)