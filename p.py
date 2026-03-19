word=input('enter your word: ') 

reversed_word=''  

for ch in word:
    reversed_word=ch+reversed_word 
if reversed_word== word:
    print('palindrome') 
else:
    print('not palindrome')