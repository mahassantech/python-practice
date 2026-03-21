numbers = [10, 45, 23, 89, 67] 

max_number=numbers[0]
secmx_number=numbers[0]

for num in numbers: 
    if num > max_number :
        secmx_number=max_number
        max_number=num 
    else:
        if num > secmx_number and num != max_number:
            secmx_number=num 
print(secmx_number)