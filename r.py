numbers = [1,2,2,3,4,4,5] 

new_number=[]

for num in numbers: 
    if num not in new_number:
        new_number.append(num)
print(new_number)