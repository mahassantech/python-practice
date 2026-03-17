numbers = [10, 45, 23, 89, 67] 


max_number=numbers[0] 
se_max=numbers[0]

for num in numbers: 
    if num>max_number: 
        se_max=max_number
        max_number=num 
    elif num > se_max and num != max_number:
        se_max = num
print(se_max)