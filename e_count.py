numbers = [12, 7, 9, 20, 33, 40]
even_count=0
odd_count=0
for num in numbers:
    if num % 2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print(f'even:{even_count}')
print(f'odd:{odd_count}')