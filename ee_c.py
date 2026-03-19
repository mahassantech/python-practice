numbers = [10, 23, 45, 60, 33, 24] 

even_count=0 
Odd_count=0 

for num in numbers: 
    if num%2==0:
        even_count=even_count+1 
    else:
        Odd_count=Odd_count+1 
print('Even:',even_count)
print('Odd:',Odd_count)