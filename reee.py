numbers = [1,2,2,3,4,4,5] 

new=[] 

for num in numbers: 
    if num not in new:
        new.append(num)
print(new)