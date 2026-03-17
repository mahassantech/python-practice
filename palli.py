word=input('enter your word: ').lower() 
box=word[::-1]
if word==box:
    print('palindrome')
else:
    print('not palindrome')
    
    
word=input('enter your word: ').lower() 
 
revers_word='' 

for char in word:
    revers_word=char + revers_word
if revers_word==word:
    print('plaindrome') 
else:
    print('not palindrome')
